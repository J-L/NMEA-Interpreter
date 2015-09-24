from math import radians, cos, sin, asin, sqrt

class GpsPoint:
    def __init__(self, message):
        message_array = message.split(",")
        utc_time = message_array[1]
        valid = message_array[2]
        self.latitude = float(message_array[3])
        self.ns_direction = message_array[4]
        self.longitude = float(message_array[5])
        self.ew_direction = message_array[6]
        self.date_string = message_array[7]
        seconds_from_unix_to_y2k = 1442983998
        hours = int(utc_time[0:1])
        minutes = int(utc_time[2:3])
        seconds = int(utc_time[4:5])
        self.utc_seconds = seconds_from_unix_to_y2k + 3600 * hours + 60 * minutes + seconds
        print "Number of seconds from epoch: "+ str(self.utc_seconds)
        print "Latitude:                     "+ str(self.latitude)+str(self.ns_direction)
        print "Longitude:                    "+ str(self.longitude)+str(self.ew_direction)
    def __sub__(self, gps_point):
        return self.distance(self.longitude, self.latitude, gps_point.longitude, gps_point.latitude)
    def __add__(self, gps_point):
        return self._distance_(self.longitude, self.latitude, gps_point.longitude, gps_point.latitude)
    def _distance_(self,lon1, lat1, lon2, lat2):
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
        R = 6371000  # radius of the earth in km
        x = (lon2 - lon1) * cos( 0.5*(lat2+lat1) )
        y = lat2 - lat1
        self.distance= R * sqrt( x*x + y*y )
        return self.distance
    def bearing(self, something):
        pass
        
def GpsVector:
    def __init__(self, point_a, point_b):
        pass
    def __add__(self, vector_b):
        pass
    def __sub__(self, vector_b):
        pass
    def __mul__(self, vector_b):
        pass
    def calc_time(self):
        pass
    def calc_velocity(self):
        pass
        
        


class NmeaInterpreter:
    current_time = ""
    utc_time = ""
    last_longitude = 00104.0143
    last_latitude =  0105.9219
    def __init__(self,):
        pass
    def decode_GPGSV(self,message):
        pass
    def decode_GPRMC(self,message):
        #handles gps location data
        #example $GPRMC,093627,A,0105.9219,N00104.0144,W4.031.8,230915,,,A%A
        #$GPRMC,093627,A,0105.9219,N,00104.0144,W,4.0,31.8,230915,,,A*5A
        a = GpsPoint(message)
        b = GpsPoint(message)
        print a-b
        
        
        
    def decode_IIVHW(self,message):
        #handles parsing windspeed and angle
        pass
    def decode_IIDBT(self,message):
        #handles depth below transducer messages
        pass
    def decode_IIMWV(self,message):
        #decodes measured wind velocity
        pass
    def decode_IIHDG(self,message):
        #decodes measured heading
        pass
    def decode_message(self,message):
        #general method for selecting and decoding a message
        pass

        
if __name__ == "__main__":
    nmea = NmeaInterpreter()
    nmea.decode_GPRMC("$GPRMC,093627,A,0105.9219,N,00104.0144,W,4.0,31.8,230915,,,A*5A\n")