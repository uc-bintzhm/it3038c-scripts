var http = require("http");
var fs = require('fs'); //Allows to read the html that I created because I prefer htmls
const bodyParser = require("body-parser"); //research told me to add this because it kept yelling at me

fs.readFile('./index.html', function (err, html) { //reads the HTML as a file and this is what will show when the server on the port is running. 

    if (err) throw err; // noticed this error come up, and stacked overflow references this line when using fs, so that is where I got this information.    

    http.createServer(function(req, res) {  //shows the basic html index in the folder
        if (req.url === "/") {
            res.writeHeader(200, {"Content-Type": "text/html"});  
            res.write(html);  
            res.end(); 
        } 
        else if (req.url === "/snakegame") { //shows the code for snake.py
            fs.readFile('snake.py', 'utf8', function(err, data) {
                if (err) throw err;  
                res.end(data);
            });
        }
        else if (req.url === "/snakereadme") { //shows the readme info
            fs.readFile('README.md', 'utf8', function(err, data) {
                if (err) throw err;  
                res.end(data);
            });
        }
        else if (req.url === "/snakescore") {// shows the logged scores. If you click refresh after playing snake and logging a score, the server should update too. 
            fs.readFile('pythonsnake.txt', 'utf8', function(err, data) {
                if (err) throw err;  
                res.end(data);
            });
        }
        else { //does not show data. 
            res.writeHead(404, {"Content-Type": "text/plain"});      
            res.end("Data not found");        
            } 
    }).listen(3000); //has the server listening on 3000
});
console.log("Server is listening on port 3000"); //shows on the terminal that the server is listening on port 3000