const socket = require("socket.io");

const setupSocket = (server) => {
  const io = socket(server);

  io.on("connection", (socket) => {
    console.log("Socket connection is created.");

    socket.on("disconnect", () => {
      console.log("Socket is disconnected");
    });

    socket.on("anomalyEvent", () => {});

    socket.on("videoFrame", () => {});
  });
};

module.exports = setupSocket;
