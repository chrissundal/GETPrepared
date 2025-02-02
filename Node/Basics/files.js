const fs = require('fs')
const os = require("node:os");

//read files
// fs.readFile('./docs/blog1.txt', (err, data) => {
//     if (err) {
//         console.error(err)
//     }
//     console.log(data.toString())
// })
//
// console.log('last line')

//write files

// fs.writeFile('./docs/blog1.txt', 'Hello World!', () => {
//     console.log('file was changed successfully.');
// })
// fs.writeFile('./docs/blog2.txt', 'Hello Again!', () => {
//     console.log('file was created successfully.');
// })

//directory
if (!fs.existsSync('./assets')) {
    fs.mkdir('./assets', (err) => {
        if (err) {
            console.log(err);
        }
        console.log('folder created')
    })
}
else {
    console.log('already exists!');
    fs.rmdir('./assets', (err) => {
        console.log('folder removed');
    })
}
//delete files

if (fs.existsSync('./docs/deleteme.txt')) {
    fs.unlink('./docs/deleteme.txt', (err) => {
        if (err) {
            console.log(err);
        }
        console.log('file removed')
    });
}