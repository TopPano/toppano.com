# This dockerfile uses the ubuntu image

FROM ubuntu:14.04

MAINTAINER uniray7 uniray7@gmail.com

# install nodejs
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -
RUN apt-get install -y nodejs
RUN apt-get install -y build-essential

# install gearmand
RUN apt-get install -y gearman-job-server

# install graphicMagic
RUN apt-get install -y python-software-properties
RUN apt-get install -y software-properties-common 
RUN add-apt-repository -y ppa:dhor/myway
RUN apt-get update
RUN apt-get install -y graphicsmagick

# S3 access key(temperaly)

# git clone laputa-api
RUN apt-get install -y git
RUN git clone https://verpix-devops:T0ppan0@github.com/TopPano/laputa-api.git ~/laputa-api

# git clone verpix-async
RUN git clone https://verpix-devops:T0ppan0@github.com/TopPano/verpix-async.git ~/verpix-async
