"""Demonstrate scoping."""

count = 0

def show_count():
	print("count = ", count)

def set_count(c):
    """
    count = c
    """
    global count
    count = c
