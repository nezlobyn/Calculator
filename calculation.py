def add(firstnumb,secondnumb):
	return ('Answer: {}'.format(float(firstnumb)+float(secondnumb)))

def subtract(firstnumb,secondnumb):
	return ('Answer: {}'.format(float(firstnumb)-float(secondnumb)))

def divide(firstnumb,secondnumb):
	if int(secondnumb) ==0:
		return ('sorry, second numb = 0..')
	else:
		return ('Answer: {}'.format(float(firstnumb)/float(secondnumb)))

def multiply(firstnumb,secondnumb):
	return ('Answer: {}'.format(float(firstnumb)*float(secondnumb)))




def main():
	while True:
		answer = input('Choice operation: \nadd = +  subtract = -  divide = /  multiply = *\nsquare = **  square root = //\nbreak = 0\nyour choice: ')
		if answer =='0':
			break
		else:
			if answer != '+' and answer != '-' and answer != '*' and answer != '/' and answer !='**' and answer !='//':
				print("Sorry but doesn't this operation")
			elif answer == '**':
				sq = float(input('number please: '))
				print(sq**2)
			elif answer =='//':
				sq = float(input('number please: '))
				print(sq**0.5)	
			else:
				firstnumb = input('first number: ')
				secondnumb = input('second number: ')
				firstnumb = firstnumb.replace(',','.')
				secondnumb = secondnumb.replace(',','.')
				start = 0
				for i in range(len(firstnumb)):
					if ord(firstnumb[i])>57 or ord(firstnumb[i])<=45 or ord(firstnumb[i])==47:
						start+=1
						break
				for i in range(len(secondnumb)):
					if ord(secondnumb[i])>57 or ord(secondnumb[i])<45 or ord(secondnumb[i])==47:
						start+=1
						break
				if start!=0:
					print('you must print only numbers!')
				elif answer == '+':
					print(add(firstnumb,secondnumb))
				elif answer == '-':
					print(subtract(firstnumb,secondnumb))
				elif answer == '/':
					print(divide(firstnumb,secondnumb))
				elif answer == '*':
					print(multiply(firstnumb,secondnumb))





if __name__=='__main__':
	main()