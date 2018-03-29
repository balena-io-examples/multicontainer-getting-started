# Getting started with multicontainer on resin.io

This example will get you up and running quickly with a multicontainer setup on resin.io. The application creates a plot of your device's CPU load average and memory usage at the device's public URL, which is piped over using websockets. The system is composed of a simple static site server, a websocket server, and a proxy. These 3 components are defined in the [docker-compose.yml](docker-compose.yml) as services and are only given as much privilege as is needed.

To get this project up and running, you'll need to [sign up](https://dashboard.resin.io/signup) for a resin.io account, create a microservices or starter application, and provision a device (device specific instructions can be found in our [getting started guide](https://docs.resin.io/getting-started).

*Note: Multicontainer functionality requires resinOS v2.12.0 or higher. If you do not see an option to choose a microservices or starter application type, a supported OS version has not yet been released for the selected device type.*

Once you are set up, clone this repo locally:
```
$ git clone git@github.com:resin-io-projects/multicontainer-getting-started.git
```
Copy the command in the upper-right corner of your application dashboard to add your remote repository:
```
$ git remote add resin username@git.resin.io:username/myapp.git
```
Finally, push the code to the newly added remote:
```
$ git push resin master
```
It should take a few minutes for your project to build. While you wait, you can enable device URLs, so you can see the server outside of our local network. This option can be found in the *Actions* drop down in your device dashboard.
