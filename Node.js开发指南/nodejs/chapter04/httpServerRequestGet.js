var http = require('http');
var url = require('url');
var util = require('util');

http.createServer(function(req,res){
	res.writeHead(200,{'Content-Type':'text/html'});
	res.end(util.inspect(url.parse(url.parse(req.url,true))));

}).listen(3001);
//127.0.0.1:3001/user?name=elephantzhai&email=739476800@qq.com
