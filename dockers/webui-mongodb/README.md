# verpix.me webui mongodb

### Build image:
* docker build -t verpix-dev/webui-mongodb Dockerfile/path

### Run image:
* docker run -p public_port:8081 verpix-dev/webui-mongodb /bin/bash -c "python3 ~/verpix.me/dockers/webui-mongodb/setup.py &"

### Remote run:
* ssh -i "ssh.pem" user@host "sudo docker run -p 8086:8081 verpix-dev/webui-mongodb sh -c \"python3 ~/verpix.me/dockers/webui-mongodb/setup.py\" &"
