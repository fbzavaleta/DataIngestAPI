FROM ubuntu:lastest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip 

WORKDIR /usr/app

COPY . /usr/app/

RUN pip3 install -r requirements.txt
RUN chmod +x docker_entrypoint.sh

ENTRYPOINT ["/bin/bash" , "./docker_entrypoint.sh"]