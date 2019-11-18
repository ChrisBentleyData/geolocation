import cherrypy
import pandas as pd
import myprocessor

p = myprocessor.MyProcessor()

class MyWebService(object):
    
    @cherrypy.expose
    
    # Attach the json attributes to the request 
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()

    def process(self):
        print('Processing data now...')
        data = cherrypy.request.json
        print(data)
        
        #Capture the address as string from input
        addr = str(data['addr'])
        print('addr: '+ addr)
        
        #process the address 
        output = p.run(addr)     
        return output.to_json()

if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(MyWebService())