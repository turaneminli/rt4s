const express = require("express");
const cors = require("cors");
const bodyParser = require("body-parser");
const http = require("http");
const setupSocket = require("./socket");

const app = express();
const server = http.createServer(app);

setupSocket(server);

app.use(cors());
app.use(bodyParser.json());

app.use("/", mainRouter);

server.listen(5001, () => {
  console.log("The application is started over 5001.");
});
