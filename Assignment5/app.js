var awsIot = require('aws-iot-device-sdk');

var child_process = require('child_process');
var argument = process.argv;
var maxprocess = argument[2];
var i=0;
const child = [];
//
// Replace the values of '<YourUniqueClientIdentifier>' and '<YourCustomEndpoint>'
// with a unique client identifier and custom host endpoint provided in AWS IoT.
// NOTE: client identifiers must be unique within your AWS account; if a client attempts
// to connect with a client identifier which is already in use, the existing
// connection will be terminated.
//
var device = awsIot.device({
   keyPath: '9670267452-private.pem.key',
  certPath: '9670267452-certificate.pem.crt',
    caPath: 'root-ca.pem',
  clientId: 'SensorEID',
      host: 'a37k9ro04gprkh-ats.iot.us-east-1.amazonaws.com'
});


function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

//
// Device is an instance returned by mqtt.Client(), see mqtt.js for full
// documentation.
//
console.log('Device connected ..');


for(i=0;i<maxprocess;i++){
	var sendvar = i;
	var string = {};
	child[i] = child_process.fork('sensor.js');
	child[i].send(sendvar);
	child[i].on('message', (msg) => {
		console.log('listening from child process ...');
		console.log(msg);
		device
  			.on('connect', function() {
    		console.log('connect');
    		device.publish('SensorEIDPolicy', JSON.stringify(msg));
    		console.log('Message Sent ...');
  		});

		device
		  .on('message', function(topic, payload) {
		    console.log('message', topic, payload.toString());
		  });
	});
}


/*while(1){
 	sleep(100);*/

//}
/*const con = require('./db.js');
var child_process = require('child_process');


console.log(maxprocess);

if(!argument[2]){

	console.log('Try: node app.js {numerical value}');

}else{
  con.query("CREATE DATABASE IF NOT EXISTS eid", function (err, result) {
    if (err) throw err;
    console.log("Database created");
});
		var create = "CREATE TABLE IF NOT EXISTS eid.sensor (id INT, TimeStamp VARCHAR(25), sensornumber INT, Tempreture FLOAT,Humidity FLOAT, Alarm_Count_Temp INT,Alarm_Count_Hum INT, Error_Count INT)";
		con.query(create, function(err, result){
		    if (err) throw err;
		    console.log("Table created");
		});


	for(i=0;i<maxprocess;i++){
		var sendvar = i;
		child[i] = child_process.fork('sensor.js');
		child[i].send(sendvar);
		child[i].on('message', (msg) => {

  			var insert = "INSERT INTO eid.sensor VALUES ("+msg.id+",\""+msg.Timestamp+"\","+ msg.sensorid+","+ msg.Temperature+","+ msg.Humidity+","+msg.Alarm_Count_Temp+","+msg.Alarm_Count_Hum+","+msg.ErrorCount+");"
  			con.query(insert, function(err, result){
				if (err) throw err;
		    	console.log("Query Inserted");
			});
		});
	}
}
*/