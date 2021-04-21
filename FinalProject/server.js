var http = require("http");
var fs = require('fs'); //Allows to read the html that I created because I prefer htmls
const bodyParser = require("body-parser"); //research told me to add this because it kept yelling at me

fs.readFile('./index.html', function (err, html) {

    if (err) throw err;    

    http.createServer(function(req, res) {  
        if (req.url === "/") {
            res.writeHeader(200, {"Content-Type": "text/html"});  
            res.write(html);  
            res.end();
        } 
        else if (req.url === "/snakegame") {
            fs.readFile('snake.py', 'utf8', function(err, data) {
                if (err) throw err;  
                res.end(data);
            });
        }
        else if (req.url === "/snakereadme") {
            fs.readFile('README.md', 'utf8', function(err, data) {
                if (err) throw err;  
                res.end(data);
            });
        }
        else if (req.url === "/snakescore") {
            fs.readFile('pythonsnake.txt', 'utf8', function(err, data) {
                if (err) throw err;  
                res.end(data);
            });
        }
        else {
            res.writeHead(404, {"Content-Type": "text/plain"});      
            res.end("Data not found");        
            } 
    }).listen(3000); //has the server listening on 3000
});
console.log("Server is listening on port 3000");