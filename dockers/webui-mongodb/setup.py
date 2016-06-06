import os
import re
import socket

webui_mongo_config = os.environ['WEBUI_MONGO']+'/config.js'

db_name = 'verpix-dev-db'
db_ip = '52.69.111.158'
db_port = 27019
user = 'user'
passwd = 'pass'
webui_ip = socket.gethostbyname(socket.gethostname())

config_file = open(webui_mongo_config, 'r+')
text = config_file.read()
text = re.sub("\'db\'", "\'"+db_name+"\'", text)
text = re.sub("\'localhost\'", "\'"+db_ip+"\'", text)
text = re.sub('27017', str(db_port), text)
text = re.sub("\'admin\'", "\'"+user+"\'", text)
text = re.sub("\'pass\'", "\'"+passwd+"\'", text)

config_file.seek(0)
config_file.write(text)
config_file.close()

os.system('export VCAP_APP_HOST='+webui_ip+';node '+os.environ['WEBUI_MONGO']+'/app.js &')
