﻿const Blog = require("../models/blog");
const blog_index = (req,res) => {
    Blog.find().sort({ createdAt: -1 })
        .then((result) => {
            res.render("index", { title: "All Blogs", blogs: result});
        })
        .catch(err => console.log(err));
}
const blog_single = (req,res) => {
    const id = req.params.id;
    Blog.findById(id)
        .then((result) => {
            res.render("single", { title: "Blog", blog: result});
        })
        .catch(err => {
            res.status(404).render('404', { title: "Not Found" });
        });
}
const blog_create_get = (req,res) => {
    res.render('create', { title: "Create" });
}

const blog_create_post = (req,res) => {
    const newPost = new Blog(req.body);
    newPost.save()
        .then((result) => {
            res.redirect('/blogs');
        })
        .catch(err => console.log(err));
}
const blog_delete = (req,res) => {
    const id = req.params.id;
    Blog.findByIdAndDelete(id)
        .then(result => {
            res.json({redirect: '/blogs'});
        })
        .catch(err => {
            console.log(err);
        });
}
module.exports = {
    blog_index,
    blog_single,
    blog_create_post,
    blog_delete,
    blog_create_get
}