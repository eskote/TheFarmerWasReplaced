# Clear farm
if get_pos_x() or get_pos_y() != 0:
		clear()

# Intitialize plant_locations
plant_dict = {}

# Set intial value of planted
planted = False
# Begin Loop
while num_items(Items.Hay) < 500000000:
	# For each column
	for x in range (get_world_size()):
		# For each row
		for y in range(get_world_size()):
			
			# Planting logic
			current_pos = (get_pos_x(), get_pos_y())
			if current_pos in plant_dict:
				plant_type = plant_dict[current_pos]
				if can_harvest():
					harvest()
				if get_ground_type() != Grounds.Soil:
					till()
				
				# Plant
				plant(plant_type)
				
				# Remove current_pos from plant_dict{}
				plant_dict.pop(current_pos)
				planted = True
				
			# get_companion
			next_location = get_companion()
			
			# only add if value != None
			if next_location != None:
				next_plant_type, (next_x, next_y) = next_location
				plant_dict[(next_x, next_y)] = next_plant_type
				
			# Determine if Odd column
			if x % 2 == 0:
				odd_column = True
			else:
				odd_column = False
			
			# Determine if odd row
			if y % (get_world_size() / 4) == 0:
				odd_row = True
			else:
				odd_row = False
			
			# Plant a Sunflower
			if odd_column == True and odd_row == True:
				if get_ground_type() != Grounds.Soil:
					till()
				if can_harvest():
					harvest()
				plant(Entities.Sunflower)
			
			# Runs only if planted == False
			if planted == False:
				if can_harvest():
					harvest()
				plant(Entities.Grass)
			
			# Water if soil is dry
			#if get_entity_type() != Entities.Grass and get_water() < 0.5:
			#	use_item(Items.Water)
					
			move(North)
			planted = False
		move(East)