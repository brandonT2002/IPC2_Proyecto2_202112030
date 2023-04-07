let headers = new Headers()
let api = 'http://localhost:4000'
headers.append('Content-Type','application/json');
headers.append('Accept','application/json');
headers.append('Access-Control-Allow-Origin',api);
headers.append('Access-Control-Allow-Credentials','true');
headers.append('GET','POST','OPTIONS','PUT','DELETE')