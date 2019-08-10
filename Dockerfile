# This is docker file to run unittest for the whole projects.
FROM centos

# Install python and pip
RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install python-pip

RUN mkdir /transensor
ADD requirements.txt /transensor/requirements.txt
RUN pip install -r /transensor/requirements.txt

ADD . /transensor
RUN chmod 755 /transensor/scripts/*.sh

WORKDIR /transensor
