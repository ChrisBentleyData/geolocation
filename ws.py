import cherrypy
import pandas as pd
import myprocessor

p = myprocessor.MyProcessor()

class MyWebService(object):
    
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    #@cherrypy.tools.accept(media='text/plain')
    def process(self):
        print('Processing data now...')
        data = cherrypy.request.json
        print(data)
        #addr = pd.DataFrame(data)
        addr = str(data['addr'])
        print('addr: '+ addr)
        output = p.run(addr)     
        return output.to_json()

if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(MyWebService())