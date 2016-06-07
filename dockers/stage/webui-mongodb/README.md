# verpix.me webui mongodb

### Build image:
```sh
$ docker build -t verpix-dev/webui-mongodb Dockerfile/path
```

### Run image:
```sh
$ docker run -d -p public_port:8081 verpix-dev/webui-mongodb /bin/bash -c "python3 ~/verpix.me/dockers/webui-mongodb/setup.py" &
```
It will return the **container id**


### Restart container:
```sh
$ docker restart container_id
```

### Remote run:
```sh
$ ssh -i "ssh.pem" user@host "sudo docker run -p 8086:8081 verpix-dev/webui-mongodb sh -c \"python3 ~/verpix.me/dockers/webui-mongodb/setup.py\" &"
```

### Remote restart:
```sh
$ ssh -i "ssh.pem" user@host "sudo docker restart container_id"
```
