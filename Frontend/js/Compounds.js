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
                    getCompounds()
                    viewCompounds()
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
                getCompounds()
                getMachinesC()
                viewCompounds()
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

function getMachinesC(){
    let compound = document.getElementById('selectCompound').selectedIndex - 1
    document.getElementById('buildButton').innerHTML = ''
    fetch(`${api}/machinesC`,{
        method: 'POST',
        headers,
        body: `{"compound":${compound}}`
    })
    .then(response => {
        response.text().then(text => {
            let option = ''
            if(text != 'None') {
                option = '<select name="machine" id="selectMachine" class="selectMachine" onchange="putButtonBuild()"><option selected="selected" disabled="">Seleccione una Máquina</option>'
                text = `number,name,time\n${text}`;
                text = Papa.parse(text,{header:true,dynamicTyping:true,skipEmptyLines:true}).data
                for (let machine of text) {
                    option += `<option>${machine.number} - ${machine.name} - ${machine.time}s</option>`
                }
                option += '</select>'
            }
            document.getElementById('selectMachine1').innerHTML = option
        })
    })
    .catch(error => {
        // alert('Error')
    })
}

function putButtonBuild() {
    document.getElementById('buildButton').innerHTML = '<button type="button" class="button" onclick="viewStep()">Construir Compuesto</button>'
}

function getCompounds(){
    fetch(`${api}/compounds`,{
        method: 'GET',
        headers
    })
    .then(response => {
        response.text().then(text => {
            let option = '<option selected="selected" disabled="">Seleccione un Compuesto</option>'
            if(text != 'None') {
                text = `number,name,elements\n${text}`;
                text = Papa.parse(text,{header:true,dynamicTyping:true,skipEmptyLines:true}).data
                for (let machine of text) {
                    option += `<option>${machine.number} - ${machine.name}</option>`
                }
            }
            document.getElementById('selectCompound').innerHTML = option
        })
    })
    .catch(error => {
        // alert('Error')
    })
}

function viewCompounds(){
    fetch(`${api}/compounds`,{
        method: 'GET',
        headers
    })
    .then(response => {
        response.text().then(text => {
            let table = '<tr><th id="noBooks" class="center-text">No hay elementos Compuestos</th></tr>'
            if(text != 'None') {
                table = '<tr><th>ID</th><th>Compuesto</th><th>Fórumula</th></tr>'
                text = `number,name,elements\n${text}`;
                text = Papa.parse(text,{header:true,dynamicTyping:true,skipEmptyLines:true}).data
                for (let compound of text) {
                    table += `<tr>
                    <td>${compound.number}</td>
                    <td>${compound.name}</td>
                    <td>${compound.elements}</td>
                    </tr>`
                }
            }
            document.getElementById('compoundsInfo').innerHTML = table
        })
    })
    .catch(error => {
        // alert(error)
    })
}

function viewStep(){
    let compound = document.getElementById('selectCompound').selectedIndex - 1
    let machine = document.getElementById('selectMachine').selectedIndex - 1
    if (compound === -1){
        swal({
            title: "¡Oops!",
            text: "No se ha seleccionado un Compuesto",
            icon: "info",
            buttons: false,
            timer: 2000
        })
    }
    else if (machine === -1){
        swal({
            title: "¡Oops!",
            text: "No se ha seleccionado una Máquina",
            icon: "info",
            buttons: false,
            timer: 2000
        })
    }
    else{
        fetch(`${api}/compounds`,{
            method: 'POST',
            headers,
            body: `{
                "machine": ${machine},
                "compound": ${compound}
            }`
        })
        .then(response => {
            response.text().then(text => {
                // console.log(text)
                // d3.select('#machine').html('');
                d3.select('#step').graphviz().scale(2.3).height(document.getElementById('step').clientHeight).width(800*1.9).renderDot(text)
            })
        })
        .catch(error => {
    
        })
    }
}