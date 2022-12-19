from server.models import Parking

data={
    '_id' : "TW-1-1",
    'status' : "empty", # empty or inuse 
    'license_plate' : "EAC-8668",
    'position':['121.519','25.035'],
    'error':'',
    'machine' : "E01"
}
Parking.create_parking(data)
# data={
#     '_id' : "TW-1-2",
#     'status' : "empty", # empty or inuse 
#     'license_plate' : "",
#     'position':['121.519','25.033'],
#     'machine' : "E02"
# }
# Parking.create_parking(data)
# # Parking.get_parking({})