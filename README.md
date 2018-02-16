# Getting Started with Multicontainer on Resin.io

This example will get you up and running quickly with a multicontainer setup on resin.io. The application plots our devices CPU temperature on the device URL which is piped over using websockets, the system is composed of a simple static site server, a websocket server and proxy. These 3 components are defined in our [docker-compose.yml](docker-compose.yml) as services and are only given as much privileged as is needed.

To get this project up and running, you will need to signup for a resin.io account here and set up a device, have a look at our Getting Started tutorial. Once you are set up with resin.io, you will need to clone this repo locally:
```
$ git clone git@github.com:resin-projects/simple-server-node.git
```
Then add your resin.io application's remote repository to your local repository:
```
$ git remote add resin username@git.resin.io:username/myapp.git
```
and push the code to the newly added remote:
```
$ git push resin master
```
It should take a few minutes for the code to push. While you wait, lets enable device URLs so we can see the server outside of our local network. This option can be found in the Actions drop down in your device dashboard.