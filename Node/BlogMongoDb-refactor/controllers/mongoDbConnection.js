const mongoose = require('mongoose');
const dbURI = 'mongodb+srv://dbUser:ChrisSundal87@nodechris.f6sbl.mongodb.net/node-chris?retryWrites=true&w=majority&appName=nodeChris';

const connectDB = async () => {
    await mongoose.connect(dbURI);
};

module.exports = connectDB;