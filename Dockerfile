FROM cpuskarz/acitoolkit
MAINTAINER Chet Carello "cpuskarz@cisco.com"

ADD . /app

WORKDIR /app

CMD ["python", "ahs2.py"]
