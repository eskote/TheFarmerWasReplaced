# Start loop
if get_pos_x() or get_pos_y() != 0:
		clear()

# Initialize Dictionary
plant_locations = []

plant_types = [
	Entities.Tree,
	Entities.Cactus,
	Entities.Carrot,
	Entities.Pumpkin,
	Entities.Sunflower,
]

planted = False
while True:
	# For each column
	for x in range(get_world_size()):
		# For each row
		for y in range(get_world_size()):
			print(plant_types)
			# Planting logic
			for location in plant_locations[:]:
				
				# store plant_type and target_x, target_y to the current item in the loop
				plant_type, (target_x, target_y) = location
				
				# Check if current item in loop matches current drone postion
				if get_pos_x() == target_x and get_pos_y() == target_y:
					
					# We are at a position that appears in plant_locations
					if can_harvest():
						harvest()
					if get_ground_type() != Grounds.Soil:
						till()
					plant(plant_type)
					plant_locations.remove(location)
					planted = True
					break
			
			# Add current postion companion plant to plant_locations
			next_location = get_companion()
			if next_location == None:
				pass
			else:
				plant_locations.append(next_location)
			
			# Plant a random plant 
			elif not planted and get_ground_type() != Grounds.Soil:
				if can_harvest():
					harvest()
					till()
				plant(random()
				
			# Check if needs water
			if get_entity_type() != Entities.Grass and get_water() > 1:
				print('Hello')
				use_item(Items.Water)
				
			# Move north
			move(North)
			
			# Reset planted
			planted = False
			
			# Control size of plant locations
			if len(plant_locations) > 50:
				plant_locations = plant_locations[:10]

		# Move East
		move(East)