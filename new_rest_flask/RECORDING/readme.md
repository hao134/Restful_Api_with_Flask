# Docker E-book:
https://rest-apis-flask.teclado.com/docs/docker_intro/in_depth_docker_tutorial/

# run Docker
 
## docker build
```
docker build -t rest-apis-flask-python . ### docker build -t [name of docker]
```

## docker run
```
docker run -dp 5005:5000 rest-apis-flask-python   
```
### explain:
docker run -p [local port]:[docker port] [name of docker]

## this way support change local code and reply to docker code real time 
```
docker run -dp 5005:5000 -w /app -v "$(pwd):/app" flask-smorest-api
```
### explain
docker run -p [local port]:[docker port] [-w /app means work in this app] ["$(pwd):/app" means from pwd copy to /app in docker] [name of docker]

ref: https://blog.teclado.com/python-dictionary-merge-update-operators/
