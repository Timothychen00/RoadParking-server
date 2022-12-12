from server.models import Parking

data={
    '_id' : "TW-1-1",
    'status' : "empty", # empty or inuse 
    'license_plate' : "ABCD!@#",
    'machine' : "E01"
}
Parking.create_parking(data)