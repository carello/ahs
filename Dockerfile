FROM cpuskarz/acitoolkit
MAINTAINER Chet Carello "cpuskarz@cisco.com"

ADD . /app

WORKDIR /app


# Comment out the necessary python script for the build
#CMD ["python", "ahs1.py"]
CMD ["python", "ahs2.py"]

