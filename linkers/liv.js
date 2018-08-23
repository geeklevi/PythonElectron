function liv_setup() {

    document.getElementById("liv-button-setup").value = "StartThis"
    var python = require("python-shell")
    var path = require("path")
    var childProcess = require("child_process");
  
    var options = {
      scriptPath : path.join(__dirname, './engine/'),
      // pythonPath : 'C:\\Users\\LEVI\\Anaconda3\\pythonw'
      pythonPath : 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Anaconda3_64\\pythonw'
    }
  
    var liv = new python("liv.py", options);
  
    // liv.end(function(err, code, message) {
    //   document.getElementById("liv-button-setup").value = "EndThis";
    //   })
    liv.send('hello');
 
    liv.on('message', function (message) {
      // received a message sent from the Python script (a simple "print" statement)
      console.log(message);
    });
    
    // end the input stream and allow the process to exit
    liv.end(function (err,code,signal) {
      if (err) throw err;
      console.log('The exit code was: ' + code);
      console.log('The exit signal was: ' + signal);
      console.log('finished');
      console.log('finished');
    });
  
  }
  
  
  function add_face(){
    var python = require("python-shell")
    var path = require("path")
    var name = document.getElementById("person").value
  
      var options = {
      scriptPath : path.join(__dirname, '/../engine/'),
      pythonPath : '/usr/local/bin/python3',
      args : ["cam", name]
    }
  
    var face = new python("add_face.py", options);
  
    face.end(function(err, code, message) {
      swal("Face added!", "We can now recognize your face", "success")
      document.getElementsById("add").innerHTML = "Add a new face";
    })
  }