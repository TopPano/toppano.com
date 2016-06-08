# api server

### Remote run (Interactive):
```sh
$ ssh -i "ssh.pem" user@host "docker run  -i -p 3001:3000 -t verpix-dev/api-server_dev /bin/bash"
```

* run gearmand(background)
```sh
$ gearmand --log-file=/var/log/gearman-job-server/gearman.log &
```

* run verpix-async
```sh
$ cd ~/verpix-async
$ npm install
$ S3_BKT=verpix-img-development-base node start
```

* run laputa-api
```sh
$ cd ~/laputa-api
$ npm install
$ DB_URL='mongodb://@mongodb_ip:port/mongodb_name?allowExtendedOperators=true&readPreference=secondary' DB_NAME=verpix-dev-db S3_BKT=verpix-img-development-base NODE_EV=production npm start
```

