function liv_setup() {

    document.getElementById("liv-button-setup").value = "StartThis"
    var python = require("python-shell")
    var path = require("path")
    var childProcess = require("child_process");
  
    var options = {
      scriptPath : path.join(__dirname, './engine/'),
      // pythonPath : 'C:\\Users\\LEVI\\Anaconda3\\pythonw'
      pythonPath : 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Anaconda3_64\\pythonw'
      // pythonPath : 'C:\\ProgramData\\Anaconda3\\pythonw',
      
    }
  
    var main = new python("station_control/auto25.py", options);
    // liv.end(function(err, code, message) {
    //   document.getElementById("liv-button-setup").value = "EndThis";
    //   })

    // liv.send('hello');
    // main.send(JSON.stringify(
    //   {
    //     "hello": 11,
    //     "world": 22,
    //     "json": 33
    //   })
    // );
    main.on('message', function (message) {
    //   // received a message sent from the Python script (a simple "print" statement)
      console.log(message);
    //   var x = JSON.parse(message);
    //   var k = Object.keys(x);
    //   console.log(k);
    //   console.log(x.json);
    //   console.log(x["hello"]);
    });
    
    // end the input stream and allow the process to exit
    main.end(function (err,code,signal) {
      if (err) throw err;
      console.log('The exit code was: ' + code);
      console.log('The exit signal was: ' + signal);
      console.log('finished');
      console.log('finished');
    });
  
  }

  function liv_start(){


  }