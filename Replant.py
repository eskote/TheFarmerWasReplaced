# Main Planting Function
def replant(type):
	plant(type)
	
	# Don't use water if planting grass. It's not necessary.
	if type != Entities.Grass:
		if get_water() < 0.2:
			use_item(Items.Water)
	
	# Move north
	move(North) 