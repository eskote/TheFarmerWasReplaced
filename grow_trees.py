if get_pos_x() or get_pos_y() != 0:
		clear()
		
while num_items(Items.Wood) < 8000000:
	for x in range (get_world_size()):
		for y in range(get_world_size()):

			# if on odd column, return True
			if x % 2 == 0:
				odd_column = True
			else:
				odd_column = False
			
			# Returns true on y index 0 and get_world_size / 2
			if y % (get_world_size() / 2) == 0:
				odd_row = True
			else:
				odd_row = False
			
			if odd_column == True and odd_row == True:
				if get_ground_type() != Grounds.Soil:
					till()
				if can_harvest():
					harvest()
				plant(Entities.Sunflower)
			
			if get_ground_type() != Grounds.Soil:
				till()
				plant(Entities.Tree)
				
			if get_entity_type() == Entities.Tree and can_harvest():
				harvest()
				plant(Entities.Tree)
			
			if get_water() < 0.5 and get_entity_type() != Grounds.Grassland:
				use_item(Items.Water)
				
			move(North)
			
		move(East)