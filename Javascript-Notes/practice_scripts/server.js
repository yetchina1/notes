var http=require("http");
http.createServer(function(request,respone){
	respone.writeHead(200,{'Content-Type':'text/plain'});
	respone.write('Hello World!');
	respone.end();

}).listen(8888);