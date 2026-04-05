# Import ClearFarm
from ClearFarm import clear_farm

# Clears farm and resets the drone to x0, y0
clear_farm()

# Change Hat
change_hat(Hats.Dinosaur_Hat)

for x in range (get_world_size()):
	for y in range(get_world_size()):
		if get_ground_type() == Grounds.Grassland:
			harvest()
			till()
		move(North)
	move(East)

for x in range (get_world_size()):
	for y in range(get_world_size()):
		if get_ground_type() == Grounds.Grassland:
			harvest()
			till()
		move(South)
	move(West)
