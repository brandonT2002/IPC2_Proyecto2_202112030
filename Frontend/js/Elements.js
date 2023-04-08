function uploadFile(file){
	if (file){
		let reader = new FileReader()
		reader.readAsText(file,'utf-8')
		reader.onload = function(evt){
			let xml = evt.target.result.toString()
            xml = xml.replace(/"/g,'\\"')
            xml = xml.replace(/\r?\n|\r/g,'')
            fetch(`${api}/uploadFile`,{
                method : 'POST',
                headers,
                body: `{"xml": "${xml}"}`
            })
            .then(response => {
                response.text().then(text => {
                    // alert(`${text}: ${file.name}`)
                    swal({
                        title: "¡Bien!",
                        text: `${text}: ${file.name}`,
                        icon: "success",
                        buttons: false,
                        timer: 2000
                    })
                    viewElements()
                })
            })
            .catch(error => {
                // alert('Error')
            })
		}
	}
}

function reset(){
    swal({
        title: "¿Estás seguro?",
        text: "Una vez eliminado, no podrá recuperar la información",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })
    .then((willDelete) => {
        if (willDelete) {
            deleteInfo()
            swal("¡Sistema Restaurado!", {
                icon: "success",
                buttons: false,
                timer: 2000
            });
        }
    });
}

function deleteInfo(){
    fetch(`${api}/reset`, {
        method: 'DELETE',
        headers
    })
    .then(response => {
        response.text().then(text => {
            if(text == 'Sistema Restaurado'){
                viewElements()
            }
        })
    })
    .catch(error => {
        swal({
            title: "¡Oops!",
            text: "Ha ocurrido un error, no se pudo eliminar el prestamista",
            icon: "error",
        });
    })
}

function viewElements(){
    fetch(`${api}/elements`,{
        method: 'GET',
        headers
    })
    .then(response => {
        response.text().then(text => {
            let table = '<tr><th id="noBooks" class="center-text">No hay elementos registrados</th></tr>'
            if(text != 'None') {
                table = '<tr><th>Número Atómico</th><th>Símbolo</th><th>Elemento</th></tr>'
                text = `number,symbol,name\n${text}`;
                text = Papa.parse(text,{header:true,dynamicTyping:true,skipEmptyLines:true}).data
                for(let element of text) {
                    table += `<tr>
                    <td>${element.number}</td>
                    <td>${element.symbol}</td>
                    <td>${element.name}</td>
                    </tr>`
                }
            }
            document.getElementById('elementsInfo').innerHTML = table
        })
    })
    .catch(error => {
        // alert(error)
    })
}

function newElement(){
    let atomicNumb = document.getElementById('atomicNum').value
    let symbol = document.getElementById('symbol').value
    let element = document.getElementById('element').value
    if (atomicNumb.replace(' ','') == '' || symbol.replace(' ','') == '' || element.replace(' ','') == ''){
        swal({
            title: "¡Oops!",
            text: "Todos los campos son obligatorios",
            icon: "info",
            buttons: false,
            timer: 2000
        })
        return
    }
    fetch(`${api}/elements`,{
        method: 'POST',
        headers,
        body: `{
            "atomicNum": "${atomicNumb}",
            "symbol": "${symbol}",
            "name": "${element}"
        }`
    })
    .then(response => [
        response.text().then(text => {
            if (text == 'Elemento registrado'){
                swal({
                    title: "¡Bien!",
                    text: `${text}`,
                    icon: "success",
                    buttons: false,
                    timer: 2000
                })
                resetModal()
                viewElements()
            }
            else{
                swal({
                    title: "¡Noop!",
                    text: `${text}`,
                    icon: "warning",
                    buttons: false,
                    timer: 2000
                })
            }
        })
    ])
    .catch(error => {
        swal({
            title: "¡Oops!",
            text: "Ocurrió un error",
            icon: "info",
            buttons: false,
            timer: 2000
        })
    })
}

function resetModal(){
    document.getElementById('atomicNum').value=''
    document.getElementById('symbol').value=''
    document.getElementById('element').value=''
    window.location.href = 'Elementos.html#close'
}