while num_items(Items.Carrot) < 2500:
	for i in range(get_world_size()):
		if get_ground_type() == Grounds.Soil:
			if can_harvest():
				harvest()
				#plant(Entities.Carrot)
				#use_item(Items.Water)
			elif not can_harvest():
				plant(Entities.Carrot)
				use_item(Items.Water)
		elif get_ground_type() != Grounds.Soil:
			till()
			plant(Entities.Carrot)	
		move(North)	
	move(West)
		
