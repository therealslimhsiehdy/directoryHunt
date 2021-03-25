#!/bin/bash

# This script essentially asks for a directory path for the GET call to run with
# I am assuming the user already has docker downloaded and we do a quick cleanup after 

echo "Hi there! Please provide a valid directory path for me to use."

read pathName

if [[ ! -e $pathName ]]
then
	echo "That path does not exist"
	exit 1
fi

echo "To confirm, your path is $pathName"

# If dircontainer container exists, remove it.
existing_app_container=`docker ps -a | grep dircontainer | wc -l`
if [ $existing_app_container -gt "0" ]
then
    docker rm -f dircontainer
fi

# If image for dircontainer exists, remove it.
existing_app_image=`docker images | grep dirimage | wc -l`
if [ $existing_app_image -gt "0" ]
then
    docker rmi -f dirimage
fi

docker build -t dirimage .

docker run --name dircontainer -v $pathName:/mnt/mydata -p 80:80 dirimage
