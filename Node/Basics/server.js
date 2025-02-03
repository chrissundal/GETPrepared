const http = require('http')
const fs = require('fs')
const _ = require('lodash')

const server = http.createServer((req, res) => {
    //lodash
    // const num = _.random(1, 20)
    // console.log(num)
    // const greet= _.once(() => {
    //     console.log('Hello')
    // })
    // greet()
    res.setHeader('Content-Type', 'text/html')
    // res.write('<p>Hello World</p>');
    // res.write('<p>Hello again World</p>');
    // res.end();
    let path = './views/';
    switch(req.url) {
        case '/':
            path += 'index.html';
            res.statusCode = 200;
            break;
        case '/about':
            path += 'about.html';
            res.statusCode = 200;
            break;
        case '/about-me':
            res.statusCode = 301;
            res.setHeader('Location', '/about');
            break;
        default:
            path += '404.html';
            res.statusCode = 404;
            break;
    }
    fs.readFile(path, 'utf8', (err, data) => {
        if (err) {
            console.log(err)
            res.end();
        } else {
            //res.write(data)
            
            res.end(data)
        }
    })
})
server.listen(3000, 'localhost', () => {
    console.log('listening for request on port 3000')
});