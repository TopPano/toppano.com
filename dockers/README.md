# verpix.me docker compose

### Prerequisite 
Install python dependencies:
```sh
sudo apt-get install python-yaml
```
Install docker: https://docs.docker.com/engine/installation/   
Install docker-compose: https://docs.docker.com/compose/install/
### Configuration:
configs is for 4 services: 
- verpix-web-app 
- laputa-api
- verpix-async
- laputa-db

```sh
vim configs
```
Each services have properties: "branch", "commit" and "public_port".
The first 2 properties are for developer to specify the version of service.
The "public_port" is to map the service to host's port.

For example:
```python
[verpix-web-app]
branch =         
commit =
public_port = 8001
```
It means you can access the [verpix-web-app] service through http://host_ip:8081


### Setup:
```sh
python setup.py
```

### Build or rebuild all services:
```sh
docker-compose build
```
### Start:
```sh
docker-compose up -d [SERVICE_NAME]
```
**SERVICE_NAME**
- **verpix-dev-mongodb**: only mongodb contains sample data
- **verpix-dev-webui-mongodb**: webui with mongodb
- **verpix-dev-laputa-api**: api server with mogodb and webui
- **verpix-dev-web-app**: web app with api server, mongodb and webui

For example:
```sh 
docker-compose up -d verpix-dev-mongodb
```

### Observe logs
```sh 
docker-compose logs [SERVICE_NAME]
```

### Stop
```sh 
docker-compose stop [SERVICE_NAME]
```
### Remove stopped service 
```sh 
docker-compose rm
```




