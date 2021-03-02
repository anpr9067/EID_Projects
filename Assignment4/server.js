    // Node.js WebSocket server script
    const con = require('./db.js');
    const http = require('http');
    const WebSocketServer = require('websocket').server;
    const server = http.createServer();
    var finalresult1;
    var finalresult2;
    server.listen(9898);
    const wsServer = new WebSocketServer({
        httpServer: server
    });
    wsServer.on('request', function(request) {
        const sensordata0 = "SELECT * FROM eid.sensor where sensornumber = 0 ORDER BY id DESC LIMIT 10;";
        const sensordata1 = "SELECT * FROM eid.sensor where sensornumber = 1 ORDER BY id DESC LIMIT 10;";
        
        con.query(sensordata0, function(err, result, fields){
            if (err) throw err;
            console.log("query success");
            //console.log(result);
            finalresult1 = result;
            
        });
        con.query(sensordata1, function(err, result, fields){
            if (err) throw err;
            console.log("query success");
            //console.log(result);
            finalresult2 = result;
            
        });

        const connection = request.accept(null, request.origin);
        connection.on('message', function(message) {
          console.log(finalresult1);
          console.log('Received Message:', message);;
          connection.send(JSON.stringify(finalresult1));
          connection.send(JSON.stringify(finalresult2));
        });
        connection.on('close', function(reasonCode, description) {
            console.log('Client has disconnected.');
        });
    });