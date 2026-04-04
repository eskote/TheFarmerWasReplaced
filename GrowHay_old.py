# Grow Hay

def grow_hay():

	for x in range(get_world_size()):
		for y in range(get_world_size()):
			# Determine if Odd column
			if get_pos_x() % 2 == 0:
				odd_column = True
			else:
				odd_column = False
			
			# Determine if odd row
			if get_pos_y() % 2 == 0:
				odd_row = True
			else:
				odd_row = False
			
			# Water if low
			if get_entity_type() != Entities.Grass and get_water() < 0.7:
				use_item(Items.Water)
				
			# Plant and harvest Tree
			if odd_column and odd_row:
				# Till soil and plant tree if grass
				if get_entity_type() == Entities.Grass:
					till()
					
				# Harvest Tree
				elif get_entity_type() == Entities.Tree and can_harvest():
					harvest()
				plant(Entities.Tree)
					
			# Plant and harves carrot
			if not odd_column and not odd_row:
				# If grass, till
				if get_entity_type() == Entities.Grass:
					till()
				# harvest
				if can_harvest():
					harvest()
				plant(Entities.Carrot)
				
			# Plant and harvest pumpkin
			if not odd_column and odd_row:
				if get_entity_type() == Entities.Grass:
					till()
				# harvest
				if can_harvest():
					harvest()
				plant(Entities.Pumpkin)
			
			# Plant and harvest sunflower
			if odd_column and y == 0 or y == 5 or y == 11:
				if get_entity_type() == Entities.Grass:
					till()
					plant(Entities.Sunflower)
				if get_entity_type() == Entities.Sunflower and can_harvest():
					petals = measure()
					if 6 < petals < 16:
						harvest()
						plant(Entities.Sunflower)
	
			# Harvest Grass	
			if get_entity_type() == Entities.Grass and can_harvest():
				harvest()
			
			plant_type = get_companion()
			quick_print(get_companion)
			# Move North
			move(North)
			
		# Move East	
		move(East)