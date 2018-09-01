const express = require('express');
const bodyParser = require('body-parser');
const methodOverride = require('method-override');


const app = express();

app.use(express.static('./client/static/'));
app.use(express.static('./client/dist/'));


// Middleware
app.use(bodyParser.json());
app.use(methodOverride('_method'));


const port = 5010;

app.listen(port);