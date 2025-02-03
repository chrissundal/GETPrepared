const express = require('express');
const sql = require('mssql');
const app = express();

const config = {
    user: 'christoffer',
    password: 'test',
    server: 'localhost\\MSSQLSERVER01',
    database: 'MyBlogs',
    options: {
        trustServerCertificate: true,
        encrypt: true
    }
};

app.set('view engine', 'ejs');
app.listen(3000);
app.use(express.static('public'));


app.get("/", async (req, res) => {
    try {
        const conn = await sql.connect(config);
        console.log('Connected to the database');
        const result = await conn.request().query('SELECT * FROM blogs');
        const blogs = result.recordset;
        res.render("index", { title: "Home", blogs });
    } catch (err) {
        console.log('Error fetching blogs:', err);
        res.status(500).send('Error fetching blogs');
    }
});

app.get("/about", (req, res) => {
    res.render("about", { title: "About" });
});

app.get("/blogs/create", (req, res) => {
    res.render('create', { title: "Create" });
});

app.use((req, res) => {
    res.status(404).render("404", { title: "Not found" });
});
