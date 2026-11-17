# Getting started with multicontainer on balena

[![balena deploy button](https://www.balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/balena-io-examples/multicontainer-getting-started)

This is the [Docker Compose getting started guide](https://docs.docker.com/compose/gettingstarted/) running on balenaOS. It's a tiny Flask web app that counts how many times you've refreshed the page, with the count stored in Redis.

If you've done the Docker guide, the code will look very familiar. The point is to show how little has to change to get a standard Compose project onto a fleet of edge devices.

## What's in here

- `web/`: the Flask app (`app.py`), its `requirements.txt` and a `Dockerfile`
- `docker-compose.yml`: two services, `web` and `redis`
- `balena.yml`: fleet metadata used by the deploy button and balenaHub

Every refresh calls `INCR hits` in Redis and shows the new value:

```
Hello from balena! I have been seen 3 time(s).
```

## Deploy it

### With the button

Click **Deploy with balena** above. It creates a fleet in your [balenaCloud](https://dashboard.balena-cloud.com/signup) account and builds the release for you. Then add a device to the fleet and flash it, following the [getting started guide](https://docs.balena.io/learn/getting-started/raspberrypi4-64/) for your board.

### With the balena CLI

Install the [balena CLI](https://docs.balena.io/reference/balena-cli/latest/), create a fleet, then from this directory:

```bash
balena login
balena push <your-fleet>
```

Once the release has built and your device has downloaded it, switch on the **Public device URL** in the device dashboard and open it. Or browse to the device's IP on your local network, on port 80.

Little pro-tip: while you're iterating, put the device into [local mode](https://docs.balena.io/learn/develop/local-mode/) and run `balena push <device-ip>` to build and run on the device directly, without going through the cloud builders.

### Locally with Docker

The same composition runs on your laptop:

```bash
docker compose up
```

Then open <http://localhost>.

## What changed from the Docker guide

Not much, which is the nice bit:

- **No `.env` file.** balena doesn't read them. `REDIS_HOST` and `REDIS_PORT` are set in `docker-compose.yml`, and you can override them per fleet or per device as [environment variables](https://docs.balena.io/learn/manage/variables/) in the dashboard.
- **Port 80 instead of 8000.** The public device URL proxies port 80, so `web` maps `80:5000`.
- **No `--debug` flag.** The Flask debugger allows code execution from the browser. That's fine on your laptop, much less fine on a device with a public URL.
- **A retry loop in `app.py`.** balena honours `depends_on` for start order, but Redis can still be warming up when the first request lands. The app retries a few times rather than throwing an error.
- **Redis saves more often.** Devices lose power without warning, so `redis-server --save 60 1` snapshots to the `redis-data` volume once a minute if the count has changed.
- **Redis sits on an internal network.** Only `web` can reach it, and it has no route out of the device.
- **Pinned Redis image.** `redis:7.4-alpine` rather than `redis:alpine`, so a new major version can't sneak into a release.
- **`version: "2.1"`** at the top of the composition. balena supports a [subset of the Compose fields](https://docs.balena.io/reference/supervisor/docker-compose/), so check that page before reaching for anything exotic. Docker Compose on your laptop will warn that `version` is obsolete, which is safe to ignore.

The `web` service uses a plain `Dockerfile` because `python:3.12-alpine` is a multi-arch image. You only need a `Dockerfile.template` when you have to pick a different base image per architecture.

## Learn more

- [Docker Compose getting started](https://docs.docker.com/compose/gettingstarted/)
- [Multicontainer apps on balena](https://docs.balena.io/learn/develop/multicontainer/)
- [docker-compose.yml fields balena supports](https://docs.balena.io/reference/supervisor/docker-compose/)
- [balena.yml and the deploy button](https://docs.balena.io/learn/deploy/deploy-with-balena-button/)
