FROM balenalib/%%BALENA_MACHINE_NAME%%-debian-node:10-stretch-run
# Defines our working directory in container
WORKDIR /usr/src/app

RUN install_packages wget

ENV JQUERY_VERSION=3.3.1
ENV REQUIREJS_VERSION=2.3.5
ENV HIGHCHARTS_VERSION=7.0.3
RUN mkdir -p static/js && \
    wget "https://code.jquery.com/jquery-${JQUERY_VERSION}.min.js" -O static/js/jquery.min.js && \
    wget "https://code.highcharts.com/${HIGHCHARTS_VERSION}/highcharts.js" -O static/js/highcharts.js && \
    wget "http://requirejs.org/docs/release/${REQUIREJS_VERSION}/minified/require.js" -O static/js/require.js

# Copies the package.json first for better cache on later pushes
COPY package.json package.json

# This install npm dependencies on the resin.io build server,
# making sure to clean up the artifacts it creates in order to reduce the image size.
RUN JOBS=MAX npm install --production
# This will copy all files in our root to the working  directory in the container
COPY . ./

# server.js will run when container starts up on the device
CMD ["npm", "start"]
