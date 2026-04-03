# Getting started with multicontainer on balena

This example will get you up and running quickly with a multicontainer setup on balena. The application creates a simple chart of your device's CPU usage at the device's public URL (and also shows the 1-minute load average). The system is composed of a Python data API, a Streamlit frontend, and a proxy. These 3 components are defined in the [docker-compose.yml](docker-compose.yml) as services and are only given as much privilege as is needed.

Because `depends_on` is not supported by balena, startup ordering is handled with shared `flock` lock files on a named volume. Each container has a small bash startup script that waits for required dependency locks before starting.

To get this project up and running, you'll need to [sign up](https://dashboard.balena-cloud.com/signup) for a balena account, create a microservices or starter application, and provision a device (device specific instructions can be found in our [getting started guide](https://balena.io/docs/getting-started).

*Note: Multicontainer functionality requires balenaOS v2.12.0 or higher. If you do not see an option to choose a microservices or starter application type, a supported OS version has not yet been released for the selected device type.*

Once you are set up, clone this repo locally:
```
$ git clone git@github.com:balena-io-projects/multicontainer-getting-started.git
```
From the project directory, push the code to your balena application with the balena CLI:
```
$ balena push <org-name>/<app-name>
```
It should take a few minutes for your project to build. While you wait, you can enable device URLs, so you can see the server outside of our local network. This option can be found in the *Actions* drop down in your device dashboard.
