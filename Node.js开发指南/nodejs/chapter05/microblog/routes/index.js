var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
	res.render('index', { title: 'Express' });
});

router.get('/hello',function(req,res,next){
	res.send('The time is '+new Date().toString());
});
router.get('/list',function(req,res,next){
	res.render('list',{
		title:'List',
		items:[1991,'elephant','express','nodejs']
	});
});
router.get('/helper',function(req,res,next){
	res.render('helper',{
		title:'Helpers'
	})
});

module.exports = router;
