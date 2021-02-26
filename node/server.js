var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');

var server = http.createServer(function(req, res){
  if (req.url === "/") {
    fs.readFile("./public/index.html", "UTF-8", function(err, body){
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  }
  else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    freeMem=Math.round(os.freemem()/1048576);
    totalMem=Math.round(os.totalmem()/1048576);
    CPUs=os.cpus();
    numCPU=CPUs.length;
    var ut_sec = os.uptime(); 
    var ut_min = ut_sec/60; 
    var ut_hour = ut_min/60;
    var ut_day = ut_hour/60; 
      
    ut_sec = Math.floor(ut_sec); 
    ut_min = Math.floor(ut_min); 
    ut_hour = Math.floor(ut_hour); 
    ut_day = Math.floor(ut_day);
      
    ut_day= ut_day%60;
    ut_hour = ut_hour%60; 
    ut_min = ut_min%60; 
    ut_sec = ut_sec%60; 
    html=`    
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: ${ut_day} Day(s), ${ut_hour} Hour(s), ${ut_min} Minute(s), and ${ut_sec} Second(s)</p>
        <p>Total Memory: ${totalMem} MB</p>
        <p>Free Memory: ${freeMem} MB</p>
        <p>Number of CPUs: ${numCPU}</p>            
      </body>
    </html>` 
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  }
  else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000")
