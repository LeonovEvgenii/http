from moving import Chassis
from geoinformation_system import Geoinformation_system
from remote_control import Remote_control
from text_analysis import Text_analysis
from calculatu_route import Calculate_route
from computer_vision import Computer_vision
from expert_system import Expert_system

def get_data():

	objects = [ X() for X in [Chassis, Geoinformation_system, Remote_control, Text_analysis, Calculate_route, Computer_vision, Expert_system]]
	
	data = {}

	for i in objects:
		
		i()
		temp = {i.__class__.__name__:i.get()}
		data.update(temp)
		
	return data


if __name__ == '__main__':
	print(get_data())