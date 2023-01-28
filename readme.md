
docker build -t myimage .

docker container run -d -p 8080:80 nginx

docker run -d --name mycontainer -p 80:80 myimage