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
                    getMachines()
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
                getMachines()
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

function getMachines(){
    fetch(`${api}/machine`,{
        method: 'GET',
        headers
    })
    .then(response => {
        response.text().then(text => {
            option = '<option selected="selected" disabled="">Seleccione una Máquina</option>'
            if(text != 'None') {
                text = `number,name\n${text}`;
                text = Papa.parse(text,{header:true,dynamicTyping:true,skipEmptyLines:true}).data
                for (let machine of text) {
                    option += `<option>${machine.number} - ${machine.name}</option>`
                }
            }
            document.getElementById('selectMachine').innerHTML = option
        })
    })
    .catch(error => {
        // alert('Error')
    })
}

function viewMachine(){
    let index = document.getElementById('selectMachine').selectedIndex - 1
    if (index === -1){
        swal({
            title: "¡Oops!",
            text: "No se ha seleccionado una Máquina",
            icon: "info",
            buttons: false,
            timer: 2000
        })
    }
    else{
        fetch(`${api}/machine`,{
            method: 'POST',
            headers,
            body: `{"dot": ${index}}`
        })
        .then(response => {
            response.text().then(text => {
                // console.log(text)
                // d3.select('#machine').html('');
                d3.select('#machine').graphviz().scale(2.3).height(document.getElementById('machine').clientHeight).width(800*1.9).renderDot(text)
            })
        })
        .catch(error => {
    
        })
    }
}