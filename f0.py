		for i in range(get_world_size()):
			if get_ground_type() == Grounds.Soil:
				if can_harvest():
					harvest()
					plant(Entities.Grass)
				elif not can_harvest():
					plant(Entities.Grass)		
			elif get_ground_type() != Grounds.Soil:
				till()
				plant(Entities.Grass)
			move(North)
		move(West) 