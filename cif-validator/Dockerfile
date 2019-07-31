FROM tools-barebone

MAINTAINER Materials Cloud Admin <info@materialscloud.org>

RUN apt-get update \
    && apt-get -y install \
    swig \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean all

COPY ./config.yaml /home/app/code/webservice/static/config.yaml
COPY ./user_templates/* /home/app/code/webservice/templates/user_templates/
COPY ./user_requirements.txt /home/app/code
RUN pip3 install -r ./user_requirements.txt


COPY ./compute/ /home/app/code/webservice/compute/
# Set proper permissions
RUN chown -R app:app $HOME
