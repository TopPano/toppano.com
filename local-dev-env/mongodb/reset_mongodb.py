#!/usr/bin/python
from ConfigParser import SafeConfigParser
from pymongo import MongoClient
import os

parser = SafeConfigParser()
parser.read('mongodb.conf')

host_ip = parser.get('mongodb', 'host_ip')
port = parser.getint('mongodb', 'port')
db_name = parser.get('mongodb', 'db_name')
account = parser.get('mongodb', 'account')
password = parser.get('mongodb', 'password')
data_json_dir = parser.get('mongodb', 'data_json_dir')

client = MongoClient(host_ip, port)
db = client[db_name]
db.authenticate(account, password)

db.drop_collection('post')
db.drop_collection('follow')
db.drop_collection('user')
db.drop_collection('userIdentity')
db.drop_collection('like')

print "finish clear db"


os.system('mongoimport -h '+host_ip+':'+str(port)+' -u '+account+' -p '+password+' -d '+db_name+' -c post --type json --file '+data_json_dir+'/post.json')
os.system('mongoimport -h '+host_ip+':'+str(port)+' -u '+account+' -p '+password+' -d '+db_name+' -c follow --type json --file '+data_json_dir+'/follow.json')
os.system('mongoimport -h '+host_ip+':'+str(port)+' -u '+account+' -p '+password+' -d '+db_name+' -c user --type json --file '+data_json_dir+'/user.json')
os.system('mongoimport -h '+host_ip+':'+str(port)+' -u '+account+' -p '+password+' -d '+db_name+' -c userIdentity --type json --file '+data_json_dir+'/userIdentity.json')
os.system('mongoimport -h '+host_ip+':'+str(port)+' -u '+account+' -p '+password+' -d '+db_name+' -c like --type json --file '+data_json_dir+'/like.json')
