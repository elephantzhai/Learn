var events = require('events');

var emitter =  new events.EventEmitter(); 

emitter.on('someEvent',function(arg1,arg2){
	console.log('listener1',arg1,arg2);
});

emitter.on('someEvent',function(arg1,arg2){
	console.log('listener2',arg1,arg2);
});

emitter.emit('someEvent','elephantzhai',19);

// emitter.emit('error');
//如果不设置error事件，发送error事件，会停止程序，打印调用栈