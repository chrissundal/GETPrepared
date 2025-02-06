const express = require('express');
const morgan = require('morgan');
const connectDB = require('./controllers/mongoDbConnection');
const blogRoutes = require('./routes/blogRoutes');

const app = express();

connectDB()
    .then(() => {
        console.log('Connected to MongoDB');
        app.listen(3000)
    })
    .catch((err) => {
        console.log('Failed to connect to the database:', err);
    });

app.set('view engine', 'ejs');

app.use(morgan('dev'));
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.redirect('/blogs');
})

app.get('/about', (req, res) => {
    res.render("about", { title: "About" });
})

app.use('/blogs', blogRoutes);

app.use(( req, res) => {
    res.status(404).render("404", { title: "Not found" });
})