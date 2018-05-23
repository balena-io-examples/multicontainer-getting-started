requirejs.config({
  paths: {
    jquery: "jquery.min",
    highcharts: "highcharts",
    socketio: "../socket.io/socket.io"
  },
  shim: {
    highcharts: {
      exports: "Highcharts",
      deps: ["jquery"]
    },
    socketio: {
      exports: "io"
    }
  }
});

// Retry failed module loading
function requireWithRetry(modules) {
  var retryInterval = 5000;
  var retryCount = 0;
  var retryOnError = function(err) {
    var failedId = err.requireModules && err.requireModules[0];
    // this is what tells RequireJS not to cache the previous failure status
    requirejs.undef(failedId);
    retryCount++;
    console.log(`Retrying module loading #${retryCount} after wait...`);
    setTimeout(function() {
      requirejs([failedId], null, retryOnError);
    }, retryInterval);
  };
  requirejs(modules, null, retryOnError);
}
// Start our main code
requireWithRetry(["main"]);
