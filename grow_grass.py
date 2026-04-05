# Clear farm
if get_pos_x() or get_pos_y() != 0:
		clear()

# Intitialize plant_locations
plant_dict = {}

# Set intial value of planted
planted = False

# cactus_pass
cactus_pass = False

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
			else:
				planted = False
					
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
			
			# Determine if pumkin_row
			if y % (get_world_size() / 2) == 0 and planted == False:
				pumpkin_row = True
			else:
				pumpkin_row= False
			
			# Determine if sunflower_row
			if y % (get_world_size() % 5) == 0:
				sunflower_row = True
			else:
				sunflower_row = False
			
			# Plant a pumkin
			if odd_column == True and pumpkin_row == True:
				if get_ground_type() != Grounds.Soil:
					till()
				if can_harvest():
					harvest()
				plant(Entities.Pumpkin)
			
			# Plant a Sunflower
			if odd_column == False and sunflower_row == True and y % 4 == 0:
				if get_ground_type() != Grounds.Soil:
					till()
				if can_harvest():
					harvest()
				plant(Entities.Sunflower)
				cactus_pass = True
				
			# Runs only if planted == False
			if planted == False:
				if get_ground_type() == Grounds.Grassland:
					till()
				if can_harvest() and cactus_pass == True:
					harvest()
					plant(Entities.Cactus)
					cactus_pass = False
				elif can_harvest() and cactus_pass == False:
					harvest()
					plant(Entities.Pumpkin)
				if get_entity_type() == None or get_entity_type() == Entities.Dead_Pumpkin:
					plant(Entities.Pumpkin)
			
			# Water if soil is dry
			#if get_entity_type() != Entities.Grass and get_water() < 0.5:
			#	use_item(Items.Water)
					
			move(North)
		move(East)