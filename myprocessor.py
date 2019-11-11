class MyProcessor:
    def run(self, addr):   
        import pandas as pd
        import googlemaps
        import psycopg2
        
        google_api_key = ''
        dbname = 'GISDemo'
        user = ''
        password = ''
        shape_table = 'public.cb_2018_us_state500k2'
        
        gmaps = googlemaps.Client(key=google_api_key)
        
        # Geocoding the address
        geocode_result = gmaps.geocode(addr)
        
        lat = str(geocode_result[0]['geometry']['location']['lat'])
        lng = str(geocode_result[0]['geometry']['location']['lng'])
        
        conn_str = 'dbname=' + dbname + ' user=' + user + ' password=' + password
        conn = psycopg2.connect(conn_str)
        
        cur = conn.cursor()
        qry = "Select name FROM " + shape_table + " where st_intersects(geom, ST_SetSrid(ST_GeomFromText('POINT(" + lng + " " + lat + ")'),4269))"
        cur.execute(qry)
        state = cur.fetchone()[0]
        cur.close()
        
        return pd.DataFrame({'State':[state]})