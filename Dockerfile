FROM python:3.9
WORKDIR .

ENV TZone=Asia/Kolkata	
RUN ln -snf "/usr/share/zoneinfo/$TZone" /etc/localtime	
RUN echo "$TZone" > /etc/timezone	

RUN apt-get update	
RUN apt-get install -y tzdata	
RUN apt-get -qq update	
RUN apt-get -qq install -y git python3 python3-pip \
    curl pv jq nginx npm

RUN apt install npm -y

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
CMD ["bash", "run.sh"]
