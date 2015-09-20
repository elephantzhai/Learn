var fs = require('fs');

fs.readFile('content.txt','utf-8',function(err,data){
	if(err){
		console.log(err);
	}else{
		console.log(data);
	}
});


//一位一位读，不推荐

fs.open('content.txt','r',function(err,fd){
	if(err){
		console.log(err);
		return;
	}

	var buf = new Buffer(8);
	fs.read(fd,buf,0,8,null,function(err,bytesRead,buffer){
		if(err){
			console.log(err);
			return;
		}

		console.log('bytesRead: '+bytesRead);
		console.log(buffer)
	});
});


