# Grow Item
# Import Replant
from Replant import replant

# Main GrowItem function
def grow(type):
	for i in range(get_world_size()):
		if get_ground_type() == Grounds.Soil:
			if can_harvest():
				harvest()
				replant(type)
			else:
				replant(type)
		if get_ground_type() != Grounds.Soil:
			till()
			plant(type)

			# Don't use water if planting grass
			if type != Entities.Grass:
				if get_water() == 0.2:
					use_item(Items.Water)
			move(North)
	move(West)