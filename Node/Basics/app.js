const express = require('express');
const morgan = require('morgan');
const app = express();
//register view engine
app.set('view engine', 'ejs');
//app.set('views', 'myviews');

//listen for request
app.listen(3000);
//middleware & static files

app.use(morgan('dev'));
app.use(express.static('public'));
app.get("/", (req, res) => {
    //res.send('homepage');
    //res.sendFile('./views/index.html', { root: __dirname });
    const blogs = [
        {title: 'Yoshi finds eggs', snippet: 'Lorem ipsum dolor sit amet, consectetur.'},
        {title: 'Mario finds stars', snippet: 'Lorem ipsum dolor sit amet, consectetur.'},
        {title: 'How to defeat Bowser', snippet: 'Lorem ipsum dolor sit amet, consectetur.'},
    ];
    res.render("index", { title: "Home", blogs});
})

app.get("/about", (req, res) => {
    //res.send("about page");
    //res.sendFile('./views/about.html', { root: __dirname });
    res.render("about", { title: "About" });
})

//redirect
// app.get("/about-us", (req, res) => {
//     res.redirect(`/about`);
// })
app.get("/blogs/create", (req, res) => {
    res.render('create', { title: "Create" });
})

//404
// app.get("*", (req, res) => {
//     res.sendFile('./views/404.html', { root: __dirname });
// })
app.use(( req, res) => {
    //res.status(404).sendFile('./views/404.html', { root: __dirname });
    res.status(404).render("404", { title: "Not found" });
})