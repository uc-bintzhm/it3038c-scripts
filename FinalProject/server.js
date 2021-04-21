var http = require("http");
var fs = require('fs'); //Allows to read the html that I created because I prefer htmls
const { text } = require("body-parser");
//var data = require("C:/Users/madis/OneDrive/Documents/it3038c-scripts/node/public/widgets.json"); will be location of new data/scores

fs.readFile('./index.html', function (err, html) {

    if (err) throw err;    

    http.createServer(function(req, res) {  
        if (req.url === "/") {
            res.writeHeader(200, {"Content-Type": "text/html"});  
            res.write(html);  
            res.end();
        } 
        else if (req.url === "/snake") {
            fs.readFile('pythonsnake.txt', 'utf8', function(err, data) {
                if (err) throw err;
                res.writeHeader(200, {"Content-Type": "text/html"});  
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