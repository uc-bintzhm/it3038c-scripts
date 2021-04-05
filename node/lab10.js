var config = require('config')
var express = require('express')
var app = express()
var http = require("http");

app.set('port', (process.env.PORT || 3000))
app.use(express.static(__dirname + '/public'))
var data = require("./public/widgets.json");

app.get('/', function(request, response) {
  response.send('This could work pls')
})

var server = http.createServer(function(req, res){
  if (req.url === "/"){res.end('<b>Hello World! My name is = <em>' + process.env.MYNAME + '</em <br /> My Node Environemnt is :' + config.util.getEnv('NODE_ENV') + '</em></b><p><a href="/api"> Click here for Lab 10 things </a><p>')} 
  else if (req.url === "/api"){
    res.writeHead(200, {"Content-Type": "text/json"});
    res.end(JSON.stringify(data))
    }
    else {
      res.writeHead(404, {"Content-Type": "text/plain"});      
      res.end("Data not found");        
    }
});

server.listen(3000)
console.log("Node app is running at localhost:" + app.get('port'))