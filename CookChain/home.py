import cherrypy
import mysql.connector
import os
from HTMLTemplate import Template

config =  {
		'user': 'admin',
		'password':'password',
		'host':'cookchain.c54zb7ekkufg.us-west-2.rds.amazonaws.com',
		'database':'cookchain'
}
class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        html = file("index.html").read()
        template = Template(self.renderTemplate, html)
        return template.render()
    @cherrypy.expose
    def login(self,username,password):
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        args = (username,password,'')
        cursor.callproc('sp_check_password',args)
        if(args[2] == 1):
            return "success"
        else:
            return "fail"
    @cherrypy.expose
    def create(self,username,password):
    	cnx = mysql.connector.connect(**config)
    	cursor = cnx.cursor()
    	query = ('INSERT INTO Users(username,password)' 'VALUES(%s,%s)')
    	data = (username,password)
    	cursor = execute(query,data)
    	return "username" + username + "password" + password
    @cherrypy.expose
    def creditcard(self,CCNumber,CCCode,ExpDate,CCType):
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        query = ('INSERT INTO CreditCard(CCNumber,CCCode,CCType,ExpDate' 'VALUES(%s,%s,%s,%s)')
        data = (CCNumber,CCCode,ExpDate,CCType)
        cursor = execute(query,data)
        return "CCNumber" + CCNumber + "CCCode" + CCCode + "ExpDate" + ExpDate + "CCType" + "CCType"

if __name__ == '__main__':
        conf = {
                'global': {
                'server.max_request_body_size': 0
                },
                '/': {
                        'tools.sessions.on' : True,
                        'tools.staticdir.root' : os.path.abspath(os.getcwd())
                },
                '/static': {
                        'tools.staticdir.on': True,
                        'tools.staticdir.dir': './CookChain/www'
                }
        }

cherrypy.server.socket_host = '0.0.0.0'
cherrypy.quickstart(HelloWorld(),'/',conf)
