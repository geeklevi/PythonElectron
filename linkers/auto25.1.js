var python = require("python-shell")
var path = require("path")
var childProcess = require("child_process");

var options = {
    scriptPath : path.join(__dirname, './engine/'),
    // pythonPath : 'C:\\Users\\LEVI\\Anaconda3\\pythonw'
    // pythonPath : 'C:\\Program Files (x86)\\Microsoft Visual Studio\\Shared\\Anaconda3_64\\pythonw'
    pythonPath : 'C:\\ProgramData\\Anaconda3\\pythonw',
}
let main = new python("auto25.py", options);
main.on('message', function (message) {
    //   // received a message sent from the Python script (a simple "print" statement)
      console.log(message);
});
main.send('kaishi');
// main.send('whatdoesfoxsay').end(function(err){
//     if (err) handleError(err);
//     else console.log("finished demo");
// });
// main.end(function (err,code,signal) {
//     if (err) throw err;
//     console.log('The exit code was: ' + code);
//     console.log('The exit signal was: ' + signal);
//     console.log('finished');
//     console.log('finished');
//   });

function python_shell_setup() {
    main.end(function (err,code,signal) {
        if (err) throw err;
        console.log('The exit code was: ' + code);
        console.log('The exit signal was: ' + signal);
        console.log('finished');
        console.log('finished');
      });
}

function liv_setup(){

    // main.send('whatdoesfoxsay').end(function(err){
    //     if (err) handleError(err);
    //     else console.log("finished demo");
    // });
    main.send("wulegequ?");
};

