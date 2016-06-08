import subprocess
import socket

mongodb_ip = socket.gethostbyname(socket.gethostname())
mongodb_port = 27017
log_path = '/var/log/mongodb.log'

# start mongodb & set log path
subprocess.Popen(['nohup', '/usr/bin/mongod', '--logpath', log_path])

# insert data
subprocess.Popen(['/usr/bin/mongoimport', '-h', mongodb_ip+':'+str(mongodb_port), '--db', 'verpix-dev-db', '--collection', 'post', '--type', 'json', '--file', '/root/laputa-schema/data.d/mongodb/post.json']).wait()
subprocess.Popen(['/usr/bin/mongoimport', '-h', mongodb_ip+':'+str(mongodb_port), '--db', 'verpix-dev-db', '--collection', 'follow', '--type', 'json', '--file', '/root/laputa-schema/data.d/mongodb/follow.json']).wait()
subprocess.Popen(['/usr/bin/mongoimport', '-h', mongodb_ip+':'+str(mongodb_port), '--db', 'verpix-dev-db', '--collection', 'user', '--type', 'json', '--file', '/root/laputa-schema/data.d/mongodb/user.json']).wait()
subprocess.Popen(['/usr/bin/mongoimport', '-h', mongodb_ip+':'+str(mongodb_port), '--db', 'verpix-dev-db', '--collection', 'userIdentity', '--type', 'json', '--file', '/root/laputa-schema/data.d/mongodb/userIdentity.json']).wait()
subprocess.Popen(['/usr/bin/mongoimport', '-h', mongodb_ip+':'+str(mongodb_port), '--db', 'verpix-dev-db', '--collection', 'like', '--type', 'json', '--file', '/root/laputa-schema/data.d/mongodb/like.json']).wait()

# echo mongodb_ip:port
subprocess.Popen(['echo', 'mongodb://'+mongodb_ip+':'+str(mongodb_port)]).wait()

