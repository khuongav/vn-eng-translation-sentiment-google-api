# This is docker file to run unittest for the whole projects.
FROM centos

# Install python and pip
RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install python-pip

EXPOSE 80

RUN mkdir /translation
COPY . /translation
RUN pip install -r /translation/requirements.txt

WORKDIR /translation
# Run app.py translation service when the container launches
CMD ["python", "run.py"]
