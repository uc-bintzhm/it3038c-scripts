var http = require("http");
var data = require("C:/Users/madis/OneDrive/Documents/it3038c-scripts/node/public/widgets.json");

var config = require('config')
var express = require('express')
var app = express()

app.set('port', (process.env.PORT || 3000))
app.use(express.static(__dirname + '/public'))

function listBlue(res) {
    var colorBlue = data.filter(function(item) {
        return item.color === "blue";
    });

    res.end(JSON.stringify(colorBlue));
}

var server = http.createServer(function(req, res){
    if (req.url === "/") {
        res.end('<p><a href="/og"> Click here for the OG results of lab 9 </a></p><p><a href="/blue"> Click here for blue </a></p><p><a href="/api"> Click here for Lab 10 things </a><p>');
    }
    else if (req.url === "/og"){
        res.writeHead(200, {"Content-Type": "text/json"});
        res.end(JSON.stringify(data))
    }
    else if (req.url === "/blue") {
        listBlue(res);
    }
    else if (req.url === "/api") {
        app.get('/', function(request, response) {
        response.send('<b>Hello World! My name is = <em>' + process.env.MYNAME + '</em <br /> My Node Environemnt is :' + config.util.getEnv('NODE_ENV') + '</em></b>')
        })
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});      
        res.end("Data not found");        
    }
});

server.listen(3000);
console.log("Server is listening on port 3000");

