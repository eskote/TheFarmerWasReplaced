# Grow Carrot
while True:
	for i in range(get_world_size()):
		if can_harvest():
			harvest()
		else:
			plant(Entities.Carrot)
			use_item(Items.Water)
			move(North)
	move(West)