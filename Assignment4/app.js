const con = require('./db.js');
var child_process = require('child_process');
var i=0;
const child = [];
var argument = process.argv;
var maxprocess = argument[2];
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
