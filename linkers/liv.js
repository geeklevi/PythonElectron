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
  
    liv.end(function(err, code, message) {
      document.getElementById("liv-button-setup").value = "EndThis";
      })
  
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