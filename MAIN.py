# Main Code Block
# import GrowHay
import GrowHay

# Import GrowTree
import GrowTree

from GrowItem import grow
from GrowPumpkin import grow_pumpkin

# Start loop
while True:
	if get_pos_x() and get_pos_y() != 0:
		clear()

	# Start with growing Hay. Our first items
	while num_items(Items.Hay) < 5000000:
		GrowHay.grow_hay()

	# Placeholder for growing bush
	
	# Grow Tree
	while num_items(Items.Wood) < 4000000:
		current_row = 0
		GrowTree.grow_tree()
	
	# Plant Sunflower
	while num_items(Items.Power) < 100 and num_items(Items.Carrot) < 0:
		grow(Entities.Sunflower)
	
	# Grow Pumpkin
	while num_items(Items.Pumpkin) < 500000 and num_items(Items.Carrot) > 1 and num_items(Items.Wood) > 1:
		grow_pumpkin(Entities.Pumpkin) 
		
	# Grow Carrot
	while num_items(Items.Carrot) < 50000 and num_items(Items.Wood) > 1 and num_items(Items.Hay) > 1000:
		grow(Entities.Carrot)