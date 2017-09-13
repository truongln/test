#!/usr/bin/python
import os
import json
import commands

if __name__ == "__main__":
	# Iterate over all block devices, but ignore them if they are in the
	# skippable set
	skippable = ("sr", "loop", "ram")
	devices = (device for device in os.listdir("/sys/class/block")
               if not any(ignore in device for ignore in skippable))
	#data = [{"{#DEVICENAME}": device, "{#FSNAME}": commands.getoutput('lsblk -o MOUNTPOINT -nr /dev/%s' % device)} for device in devices]
	data = []
	for device in devices:
		point = commands.getoutput('lsblk -o MOUNTPOINT -nr /dev/%s' % device)
		if "\n" not in point and "SWAP" not in point:
			data.append({"{#DEVICENAME}": device, "{#FSNAME}": point})

	print(json.dumps({"data": data}, indent=4))
