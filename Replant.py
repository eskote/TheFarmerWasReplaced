def replant(type):
	plant(type)
	if get_water() < 0.2:
		use_item(Items.Water)
	move(North)