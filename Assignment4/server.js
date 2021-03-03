const con = require('./db.js');
    const http = require('http');
    const WebSocketServer = require('websocket').server;
    const server = http.createServer();
    var finalresult1;
    var finalresult2;
    var sensorid = 0;
    server.listen(9898);
    const wsServer = new WebSocketServer({
        httpServer: server
    });
    wsServer.on('request', function(request) {
        var sensordata0 = "SELECT * FROM eid.sensor where sensornumber = "+sensorid+" ORDER BY id DESC LIMIT 10;";
        console.log(sensordata0);
        con.query(sensordata0, function(err, result, fields){
            if (err) throw err;
            console.log("query success");
            //console.log(result);
            finalresult1 = result;
            
        });

        const connection = request.accept(null, request.origin);
        
        connection.on('message', function(message) {

          console.log('Received Message:', message.utf8Data);
          sensorid = message.utf8Data;
          console.log(sensorid);
          sensordata0 = "SELECT * FROM eid.sensor where sensornumber = "+sensorid+" ORDER BY id DESC LIMIT 10;";
          con.query(sensordata0, function(err, result, fields){
            if (err) throw err;
            console.log("query success");
            //console.log(result);
            finalresult1 = result;
            
            });
          console.log(sensordata0);
          connection.send(JSON.stringify(finalresult1));
          /*connection.send(JSON.stringify(finalresult1));
          connection.send(JSON.stringify(finalresult2));*/
        });
        connection.on('close', function(reasonCode, description) {
            console.log('Client has disconnected.');
        });
    });