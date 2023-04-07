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
            options = text.split('\n')
            for (let machine of options) {
                option += `<option>${machine.replace(',',' - ')}</option>`
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
    index = document.getElementById('selectMachine').selectedIndex - 1
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
            table = '<tr><th>Número Atómico</th><th>Símbolo</th><th>Elemento</th></tr>'
            elements = text.split('\n')
            for (let element of elements) {
                element = element.split(',')
                table += `<tr>
                <td>${element[0]}</td>
                <td>${element[1]}</td>
                <td>${element[2]}</td>
                </tr>`
            }
            if (elements.length > 0){
                document.getElementById('elementsInfo').innerHTML = table
            }
        })
    })
    .catch(error => {

    })
}

function newElement(){
    atomicNumb = document.getElementById('atomicNum').value
    symbol = document.getElementById('symbol').value
    element = document.getElementById('element').value
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
            option = '<option selected="selected" disabled="">Seleccione un Compuesto</option>'
            options = text.split('\n')
            for (let machine of options) {
                option += `<option>${machine.replace(',',' - ')}</option>`
            }
            // console.log(option)
            document.getElementById('selectCompound').innerHTML = option
        })
    })
    .catch(error => {
        // alert('Error')
    })
}

function viewStep(){
    compound = document.getElementById('selectCompound').selectedIndex - 1
    machine = document.getElementById('selectMachine').selectedIndex - 1
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