# Clears farm and resets the drone to x0, y0
def clear_farm():
	if get_pos_x() or get_pos_y() != 0:
			clear()