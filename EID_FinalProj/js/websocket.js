(function($) {
  'use strict';
    /*(function() {
        const messages = document.querySelector('#messages');

        let ws;

        function showMessage(message) {
          messages.textContent += `\n\n${message}`;
          messages.scrollTop = messages.scrollHeight;
          messageBox.value = '';
        }

        function init() {
          if (ws) {
            ws.onerror = ws.onopen = ws.onclose = null;
            ws.close();
          }

          ws = new WebSocket('ws://localhost:9898');
          ws.onopen = () => {
            console.log('Connection opened!');
          }
          ws.onmessage = ({ data }) => showMessage(data);
          ws.onclose = function() {
            ws = null;
          }
    }
    sendBtn.onclick = function() {
      if (!ws) {
        showMessage("No WebSocket connection :(");
        return ;
      }

      ws.send(messageBox.value);
      showMessage(messageBox.value);
    }
    init();
  })();*/
    /*var data;
    var i=0;
    var a=0, b=0,c=0,d=0,e=0,f=0;
    var temp0 = [];
    var hum0 = [];
    var temp1 = [];
    var hum1 = [];
    var temp2 = [];
    var hum2 = [];
    var temp3 = [];
    var hum3 = [];
    var temp4 = [];
    var hum4 = [];
    var temp5 = [];
    var hum5 = [];*/
    const ws = new WebSocket('ws://localhost:9898/');
    ws.onopen = function() {
        console.log('WebSocket Client Connected');
        ws.send('Hi this is web client.');
    };
    ws.onmessage = function(e) {
        //showMessage(e.data);
        //ws.send({e});
        const messages = document.querySelector('#messages');
        function showMessage(message) {
          messages.textContent += `\n\n${message}`;
          messages.scrollTop = messages.scrollHeight;
        }
        var msg = JSON.parse(e.data);
        console.log(msg);
        /*for(i=0;i<60;i++){
          if(msg[i].sensornumber == 0){
            temp0[a] = msg[i].Tempreture;
            hum0[a] = msg[i].Humidity;
          }
          if(msg[i].sensornumber == 0){
            temp1[b] = msg[i].Tempreture;
            hum1[b] = msg[i].Humidity;
          }
          if(msg[i].sensornumber == 0){
            temp2[c] = msg[i].Tempreture;
            hum2[c] = msg[i].Humidity;
          }
          if(msg[i].sensornumber == 0){
            temp3[d] = msg[i].Tempreture;
            hum3[d] = msg[i].Humidity;
          }
          if(msg[i].sensornumber == 0){
            temp4[e] = msg[i].Tempreture;
            hum4[e] = msg[i].Humidity;
          }
          if(msg[i].sensornumber == 0){
            temp5[f] = msg[i].Tempreture;
            hum5[f] = msg[i].Humidity;
          }
        }*/
        //showMessage(e.data);
      //console.log("Received: '" + e.data + "'");
    };
   /* function loadTable(tableId, fields, data) {
    //$('#' + tableId).empty(); //not really necessary
    var rows = '';
    $.each(data, function(index, item) {
        var row = '<tr>';
        $.each(fields, function(index, field) {
            row += '<td>' + item[field+''] + '</td>';
        });
        rows += row + '<tr>';
    });
    $('#' + tableId).html(rows);
}*/
})(jQuery);