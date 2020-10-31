FROM ubuntu:latest
MAINTAINER Fausto Mora "fausto.ds.mora@gmail.com"
RUN apt-get update && apt-get install -y \
    python3.8 \
    python3-pip \
    curl
ENV FLASK_APP=app
COPY . /wl-rest-api
WORKDIR /wl-rest/api
RUN pip3 install -r /wl-rest-api/requirements.txt
EXPOSE 5000
ENTRYPOINT [ "/wl-rest-api/run_this_app.sh" ]
