def poisk(answer):
	answer = int(answer)
	start = [0,1] 
	up =0
	equal = 0
	while up<answer:
		start.append(start[-1]+start[-2])
		if start[-1]==answer:
			break
		up+=1
	return start



def main():
	while True:
		answer = input('if you want stop, push: 0\nenter number:')
		start =0
		for i in range(len(answer)):
			if ord(answer[i])>57 or ord(answer[i])<48:
				start+=1
		if start!=0:
			print('Only numbrs..')
		if start == 0:
			print(poisk(answer))

		if answer == '0':
			break

if __name__ == '__main__':
    main()