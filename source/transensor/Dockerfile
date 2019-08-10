# This is docker file to run unittest for the whole projects.
FROM centos

# Install python and pip
RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install python-pip

EXPOSE 80

RUN mkdir /transensor
COPY . /transensor
RUN pip install -r /transensor/requirements.txt

WORKDIR /transensor
# Run app.py transensor service when the container launches
CMD ["python", "run.py"]
