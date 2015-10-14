var http = require('http');

var server = new http.Server();
server.on('request',function(req,res){
	res.writeHead(200,{'Content-Type':'text/html'});
	res.write('<h1>Node.js</h>');
	res.end('<p>Hello World</p>');
});
server.listen(3000);

console.log('HTTP server is listening at port 3000');
//127.0.0.1:3000
