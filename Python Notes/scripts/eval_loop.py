def eval_loop():
	response=raw_input("Enter anything, when you want to quit enter \"done\": \n")
	while(True):
		print 'you have entered: ', eval('response')
		response = raw_input('new string: ')
		if response == 'done' or response =='Done':
			break



eval_loop()
	