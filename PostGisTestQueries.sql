/* 
Created by : C. Bentley
Description: This is a sandbox area that contains queries 
that are being used to verify the behavior and geometries for the GeoLocator application are working properly 
*/

-- Decatur, GA  ST_SetSrid(ST_GeomFromText('POINT(-84.2963123 33.7748275)'),4269)	

-- Find which state a known point is located in 
SELECT *
FROM public.cb_2018_us_state500k2 
where st_intersects(geom, ST_SetSrid(ST_GeomFromText('POINT(-84.2963123 33.7748275)'),4269));

--Use the query to visually verify geocoded point (Decatur) is found in the correct shape
SELECT name
	,geom
	,st_srid(geom) mysrid
FROM PUBLIC.cb_2018_us_state500k2
UNION
SELECT 'Decatur,Ga' name
	,ST_SetSrid(ST_GeomFromText('POINT(-84.2963123 33.7748275)'), 4269) geom
	,st_srid(ST_SetSrid(ST_GeomFromText('POINT(-84.2963123 33.7748275)'), 4269)) mysid;
																															 