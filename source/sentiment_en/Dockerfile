# This is docker file to run unittest for the whole projects.
FROM centos

# Install python and pip
RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install python-pip
RUN yum -y install curl
RUN yum -y install tar
RUN yum -y install wget
RUN yum -y install which

# Create folder on container
RUN mkdir /sentiment_en
COPY . /sentiment_en
RUN pip install -r /sentiment_en/requirements.txt

# This is docker install gcloud
RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz
RUN mkdir -p /usr/local/gcloud
RUN tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz
RUN /usr/local/gcloud/google-cloud-sdk/install.sh
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin

# activate authentication
RUN gcloud auth activate-service-account --key-file='/sentiment_en/google_application_credentials.json'
RUN gcloud config set project transensor
ENV GOOGLE_APPLICATION_CREDENTIALS '/sentiment_en/google_application_credentials.json'

EXPOSE 80

WORKDIR /sentiment_en

# Run run.py sentiment_en service when the container launches
CMD ["python", "run.py"]
