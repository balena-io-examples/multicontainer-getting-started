const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);
const {
  exec
} = require('child_process');

server.listen(8080);

const getCpuLoad = (socket) => {
  exec('cat /proc/loadavg', (err, text) => {
    if (err) {
      throw err;
    }
    // Get overall average from last minute
    const load = parseFloat(text.match(/(\d+\.\d+)\s+/)[1]);
    socket.emit('loadavg', {
      onemin: load
    });
  });
};

const getMemoryInfo = (socket) => {
  exec('cat /proc/meminfo', (err, text) => {
    if (err) {
      throw err;
    }
    // Get overall average from last minute
    const matchTotal = text.match(/MemTotal:\s+([0-9]+)/);
    const matchFree = text.match(/MemAvailable:\s+([0-9]+)/);
    const total = parseInt(matchTotal[1], 10);
    const free = parseInt(matchFree[1], 10);
    const percentageUsed = (total - free) / total * 100;
    socket.emit('memory', {
      used: percentageUsed
    });
  });
};

io.on('connection', function(socket) {
  'use strict';
  console.log('a user connected');
  let dataLoop = setInterval(function() {
    getCpuLoad(socket);
    getMemoryInfo(socket);
  }, 1000);
	socket.on('disconnect', function() {
      console.log('a user disconnected');
			clearInterval(dataLoop);
   });
});
