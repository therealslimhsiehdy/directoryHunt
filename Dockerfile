FROM ubuntu:18.04

MAINTAINER Rebecca Hsieh "rebecca.hsieh07@gmail.com"

RUN apt-get update && apt-get install -y \
        software-properties-common
    RUN add-apt-repository ppa:deadsnakes/ppa
    RUN apt-get update && apt-get install -y \
        python3.7 \
        python3-pip
    RUN python3.7 -m pip install pip
    RUN apt-get update && apt-get install -y \
        python3-distutils \
        python3-setuptools
    RUN python3.7 -m pip install pip --upgrade pip

RUN unset -v PYTHONPATH

COPY ./requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt -t /app

COPY . /app 

ENTRYPOINT ["python3"]

CMD ["/app/main.py"]