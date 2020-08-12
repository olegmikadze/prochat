require('dotenv').config()
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const busboy = require('connect-busboy');
const busboyBodyParser = require('busboy-body-parser');
const path = require('path');

const db = require('./dbconnect');

let forceVar = false;
db.sync({force: forceVar}).then(() => {
    console.log(`Drop and Resync with { force: ${forceVar} }`);
});

const app = express();

app.use(express.json({ extended: false }));
app.use(cors());
app.use(busboy());
app.use(busboyBodyParser());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

//Use routes
// app.use('/api/test', require('./routes/api/test'));


// Serve static assets in production
if (process.env.NODE_ENV === 'production') {
    // Set static folder
    app.use(express.static('client/build'));

    app.get('*', (req, res) => {
        res.sendFile(path.resolve(__dirname, 'client', 'build', 'index.html'));
    });
}

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => console.log(`Server started on port: ${PORT}`));