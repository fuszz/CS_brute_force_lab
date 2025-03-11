# CS_brute_force_lab

## Building docker container

After completing code changes, save everything. Then `docker build -t <container_name> <directory_path`. 

## Pushing container to Docker Hub
1. Bind your existing container with certain Docker Hub repo: `docker tag <existing_container_name>:latest <docker username>/<docker repo name>:latest`
2. Make sure you're logged into the docker: `docker login`
3. Push your container to Docker Hub: `docker push <username>/<docker repo name>:latest>`

## Running the container:
`docker run -p 5000:5000 docker.io/fussz/brute_force_lab:latest`
