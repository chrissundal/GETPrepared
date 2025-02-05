const express = require('express');
const morgan = require('morgan');
const mongoose = require('mongoose');
const Blog = require('./models/Blog');

const app = express();
//connect to mongoDb
const dbURI = 'mongodb+srv://dbUser:ChrisSundal87@nodechris.f6sbl.mongodb.net/node-chris?retryWrites=true&w=majority&appName=nodeChris'
mongoose.connect(dbURI)
    .then((result) => app.listen(3000))
    .catch((err) => console.log(err));
app.set('view engine', 'ejs');

app.use(morgan('dev'));
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
//mongoose routes
//routing
app.get('/', (req, res) => {
    res.redirect('/blogs');
})

app.get('/about', (req, res) => {
    res.render("about", { title: "About" });
})

app.get('/blogs/create', (req, res) => {
    res.render('create', { title: "Create" });
})
//get all blogs
app.get('/blogs', (req, res) => {
    Blog.find().sort({ createdAt: -1 })
        .then((result) => {
            res.render("index", { title: "All Blogs", blogs: result});
        })
        .catch(err => console.log(err));
})
//get blogs by id
app.get(`/blogs/:id`, (req, res) => {
    const id = req.params.id;
    Blog.findById(id)
    .then((result) => {
        res.render("single", { title: "Blog", blog: result});
    })
    .catch(err => console.log(err));
})
//post blog
app.post('/blogs', (req, res) => {
    const newPost = new Blog(req.body);
    newPost.save()
        .then((result) => {
            res.redirect('/blogs');
        })
        .catch(err => console.log(err));
})
//delete
app.delete('/blogs/:id', (req, res) => {
    const id = req.params.id;
    Blog.findByIdAndDelete(id)
        .then(result => {
            res.json({redirect: '/blogs'});
        })
        .catch(err => {
            console.log(err);
        });
});
app.use(( req, res) => {
    res.status(404).render("404", { title: "Not found" });
})