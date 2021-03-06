import pygeoip

gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat')

def printRecord(tgt):
	rec = gi.record_by_name(tgt)
	city = rec['city']
	region = rec['region_name']
	country = rec['country_name']
	longitude = rec['longitude']
	latitude = rec['latitude']

	print('[*] Target: ' + tgt + 'Geo-located')
	print('[+] '+str(city)+', '+str(region)+', '+str(country))
	print('[+] Latitude: '+str(lat)+ ', Longitude: '+str(longitude))

tgt = "173.255.226.98"
printRecord(tgt)