var exec = require("child_process").exec;
function start () {
	console.log("Request Handler 'start' was called");

	// function sleep (milliSeconds) {

	// 	var startTime = new Date().getTime();
	// 	while(new Date().getTime() < startTime + milliSeconds);
	
	// }

	// sleep(10000);

	var content = "empty";

	exec("ls -lah", function (error,stdout,stderr) {
		
		content = stdout;		
	})
	return content;



}

function upload () {
	console.log("Request Handler 'upload' was called");
	return "Hello upload";
}

exports.start=start;
exports.upload=upload;