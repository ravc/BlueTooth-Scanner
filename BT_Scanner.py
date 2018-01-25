import bluetooth
from pprint import pprint

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    print("  %s - %s" % (addr, name))
    search = input('Find services?')
    if search == 'y':
        service = bluetooth.find_service(address=addr)
        pprint(service)
    else:
        print('')
