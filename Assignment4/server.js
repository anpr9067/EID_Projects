    // Node.js WebSocket server script
    const con = require('./db.js');
    const http = require('http');
    const WebSocketServer = require('websocket').server;
    const server = http.createServer();
    var requestedhumval = 0;
    var requestedtempval = 0;
    server.listen(9898);
    const wsServer = new WebSocketServer({
        httpServer: server
    });
    wsServer.on('request', function(request) {
        const numdata = "SELECT count(*) as namecount FROM eid.sensor;";
        con.query(numdata, function(err, result, fields){
            if (err) throw err;
            console.log("query success");
            console.log(result);
            requestedhumval = result[0].namecount;
            //requestedtempval = result[0].Tempreture;
            console.log(requestedhumval);
        });

        const connection = request.accept(null, request.origin);
        connection.on('message', function(message) {
          console.log('Received Message:', message);;
          console.log(requestedhumval);
          connection.send(requestedhumval);
        });
        connection.on('close', function(reasonCode, description) {
            console.log('Client has disconnected.');
        });
    });