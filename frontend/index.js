var http = require('http');
var express = require('express');

var PORT = 80;

var app = express();
var server = http.createServer(app);

app.use(express.static(__dirname + '/static'))
server.listen(PORT, function() {
	console.log("server is listening on port", PORT);
});

