var http = require('http');
var url = require('url');
var querystring = require('querystring');

var content = querystring.stringify({
	name:'elephant',
	email:'test@qq.com',
	address:'zhonghai'
});
var hostStr = '127.0.0.1';
// var hostStr = 'www.byvoid.com';

var options = {
	// host:url.parse(hostStr).hostname,
	host:hostStr,
	port:3002,
	// host:hostStr,
	// path:'',
	// path:'/application/node/post.php',
	method:'POST',
	header:{
		'Content-Type':'application/x-www-from-urlencode',
		'Content-Length':content.length
	}
}

var req = http.request(options,function(res){
	res.setEncoding('utf8');
	res.on('data',function(data){
		console.log(data);
	})
});

req.write(content);
req.end();