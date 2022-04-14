# -*- coding: UTF-8 -*-
def countdown(i):
	print(i)
	
	for j in range(4000):
		for k in range(1000):
			pass
			
	if i<=0:
		return
	else:
		countdown(i-1)
	
countdown(100)
