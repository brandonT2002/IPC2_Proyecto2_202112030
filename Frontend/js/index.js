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
                    getMachines()
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
}

function viewMachine(){
    index = document.getElementById('selectMachine').selectedIndex - 1
    fetch(`${api}/machine`,{
        method: 'POST',
        headers,
        body: `{"dot": ${index}}`
    })
    .then(response => {
        response.text().then(text => {
            console.log(text)
            // d3.select('#machine').html('');
            d3.select('#machine').graphviz().scale(2.3).height(document.getElementById('machine').clientHeight).width(800*1.9).renderDot(text)
        })
    })
}