# python:3.12-alpine is multi-arch, so a plain Dockerfile works on every
# balena device type (no Dockerfile.template needed)
FROM python:3.12-alpine

WORKDIR /code

# Set environment variables used by the `flask` command
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install `gcc` and other dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# No `--debug` here: the Werkzeug debugger allows remote code execution,
# and the device public URL can expose this port to the internet
CMD ["flask", "run"]
