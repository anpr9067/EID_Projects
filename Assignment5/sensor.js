// 	FileName: sensor.py
// 	File Description: This file contains the program for a sensor that will record the temperature, timestamp, alarms, errors, sensor number to 
//					  mysql file
// 	Author: Nitik Gupta and Antara Prakash
// 	References: https://www.w3schools.com/js/js_loop_for.asp
// 				https://stackoverflow.com/questions/45724975/date-tolocaledatestring-is-not-a-function
//				https://stackoverflow.com/questions/14249506/how-can-i-wait-in-node-js-javascript-l-need-to-pause-for-a-period-of-time
//				https://www.sitepoint.com/delay-sleep-pause-wait/
//				https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
var sensorid;
/*
	Function Name: getRandomInt
	Description: Gives a random integer between a range
	Arguments: max and min number in range
	returns: random integer between given range
*/
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
}
/*
	Function Name: sleep
	Description: pauses the program for given number of milliseconds
	Arguments: time to pause
	returns: none
*/
function sleep(milliseconds) {
  const date = Date.now();
  let currentDate = null;
  do {
    currentDate = Date.now();
  } while (currentDate - date < milliseconds);
}

function onErr(err) {
    console.log(err);
    return 1;
}

var temperature = 40;	//Base Temperature Hard-coded
/*
	Function Name: sensor
	Description: Creates a random temperature within base for one sensor
	Arguments: base temperature and sensor number
	returns: none
*/
function sensor(num,sense)
{	
	var i;
	base = Number(num);
	base_h = 40
	sensorNum = Number(sense)
	alarm = 0
	error = 0
	rownumber=0
	while(true)
	{	var r1 = getRandomInt(1,101) // Random event generator for temperature
		if(r1>=91 && r1<=95)		// 5% chance for -3 to -8
		{
			t = base + getRandomInt(-8,-2)
		}
		else if(r1>=95 && r1<=100)		// 5% chance for 3 to 8
		{	
			t = base + getRandomInt(3,9)
		}
		else if(r1>=81 && r1<=90)		// 10% chance for error number
		{	
			t = 999
			error+=1
		}
		else
		{	
			t = base + getRandomInt(-2,2)
		}
		var r1 = getRandomInt(1,101) // Random event generator for temperature
		if(r1>=91 && r1<=95)		// 5% chance for -3 to -8
		{
			h = base_h + getRandomInt(-40,-9)
		}
		else if(r1>=95 && r1<=100)		// 5% chance for 3 to 8
		{	
			h = base_h + getRandomInt(10,41)
		}
		else if(r1>=81 && r1<=90)		// 10% chance for error number
		{	
			h = 999
			error+=1
		}
		else
		{	
			h = base_h + getRandomInt(-2,2)
		}
		var d= new Date()
		var timestamp=d.toLocaleString();
		
		var data = {
			"id" : ++rownumber,
			"Timestamp" : timestamp,
			"sensorid" : sensorNum,
			"Temperature" : t,
			"Humidity" : h,
			"Alarm_Count_Temp" : alarm,
			"Alarm_Count_Hum" : alarm,
			"ErrorCount" : error
		}

		process.send(data);	// sends data to mysql
		sleep(10000);
	};
}

process.on('message', (msg) => {  
	  	
	  	sensorid = msg;
	  	console.log("sensorid "+ sensorid);
	  	//process.send(sensorid);
	 
		sleep(1000);
		sensor(temperature, sensorid);
});