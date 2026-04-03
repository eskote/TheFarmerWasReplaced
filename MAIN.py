# Main Code Block
from GrowItem import grow
from GrowPumpkin import grow_pumpkin

while True:
	if get_pos_x() and get_pos_y() != 0:
		clear()
		
	# Grow Grass
	while num_items(Items.Hay) < 76800:
		grow(Entities.Grass)
		
	# Grow Tree
	while num_items(Items.Wood) < 10000:
		grow(Entities.Tree)
	
	# Grow Pumpkin
	while num_items(Items.Pumpkin) < 10000 and num_items(Items.Carrot) > 1 and num_items(Items.Wood) > 1:
		grow_pumpkin(Entities.Pumpkin) 
		
	# Grow Carrot
	while num_items(Items.Carrot) < 2500 and num_items(Items.Wood) > 1 and num_items(Items.Hay) > 1000:
		grow(Entities.Carrot)