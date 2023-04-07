let headers = new Headers()
let api = 'http://localhost:4000'
headers.append('Content-Type','application/json');
headers.append('Accept','application/json');
headers.append('Access-Control-Allow-Origin',api);
headers.append('Access-Control-Allow-Credentials','true');
headers.append('GET','POST','OPTIONS','PUT','DELETE')

function uploadFile(file){
	if (file){
		let reader = new FileReader()
		reader.readAsText(file,'utf-8')
		reader.onload = function(evt){
			let xml = evt.target.result.toString()
            xml = xml.replace('<?xml version="1.0" encoding="UTF-8"?>','')
            xml = xml.replace('<?xml version="1.0"?>','')
            xml = xml.replace(/\r?\n|\r/g,'')
            fetch(`${api}/uploadFile`,{
                method : 'POST',
                headers,
                body: `{"xml": "${xml}"}`
            })
            .then(response => {
                response.text().then(text => {
                    alert(`${text}: ${file.name}`)
                    swal({
                        title: "¡Bien!",
                        text: `${text}: ${file.name}`,
                        icon: "success",
                        buttons: false,
                        timer: 2000
                    })

                    getMachines()
                    viewElements()
                    viewCompounds()
                    getCompounds()
                })
            })
            .catch(error => {
                alert('Error')
            })
		}
	}
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
                options = text.split('\n')
                for (let machine of options) {
                    option += `<option>${machine.replace(',',' - ')}</option>`
                }
            }
            // console.log(option)
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

function viewElements(){
    fetch(`${api}/elements`,{
        method: 'GET',
        headers
    })
    .then(response => {
        response.text().then(text => {
            let table = '<tr><th id="noBooks" class="center-text">No hay elementos registrados</th></tr>'
            if(text != 'None') {
                console.log('ENTRA AQUÍ')
                table = '<tr><th>Número Atómico</th><th>Símbolo</th><th>Elemento</th></tr>'
                let elements = text.split('\n')
                for (let element of elements) {
                    element = element.split(',')
                    table += `<tr>
                    <td>${element[0]}</td>
                    <td>${element[1]}</td>
                    <td>${element[2]}</td>
                    </tr>`
                }
            }
            document.getElementById('elementsInfo').innerHTML = table
        })
    })
    .catch(error => {
        alert(error)
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

function getCompounds(){
    fetch(`${api}/compounds`,{
        method: 'GET',
        headers
    })
    .then(response => {
        response.text().then(text => {
            let option = '<option selected="selected" disabled="">Seleccione un Compuesto</option>'
            if(text != 'None') {
                options = text.split('\n')
                for (let machine of options) {
                    machine = machine.split(',')
                    option += `<option>${machine[0]} - ${machine[1]}</option>`
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
                let compounds = text.split('\n')
                for (let compound of compounds) {
                    compound = compound.split(',')
                    table += `<tr>
                    <td>${compound[0]}</td>
                    <td>${compound[1]}</td>
                    <td>${compound[2]}</td>
                    </tr>`
                }
            }
            document.getElementById('compoundsInfo').innerHTML = table
        })
    })
    .catch(error => {
        alert(error)
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