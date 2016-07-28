FROM cp/docker
MAINTAINER Chet Carello "cpuskarz@cisco.com"

# Install basic utilities
#RUN apt-get update
#RUN apt-get -y install git python  python-pip

ADD . /app

WORKDIR /app

CMD ["python", "ahs1.py"]
