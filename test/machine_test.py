from server.models import Machine



data={
    '_id':'E09',
    'type':'esp32cam',
    'ip':'fuckyou',
    'status':'alive',
    'mac':'44:17:93:7E:3B:7C',
}
Machine.create_machine(data)
