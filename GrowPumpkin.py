# Grow Pumpkin
from Replant import replant
def grow_pumpkin(type):
	for i in range(get_world_size()):
		if get_ground_type() == Grounds.Soil:
			if not can_harvest():
				plant(type)
				replant(type)
			else:
				harvest()
		if get_ground_type() != Grounds.Soil:
			till()
			plant(type)
			if get_water() == 0.2:
				use_item(Items.Water) 
			move(North)
	move(West)