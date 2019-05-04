def compute(cost,money):
	cost = float(cost)
	money = float(money)
	if cost>money:
		return('Dont have money? get away...')
	else:
		dollars = int(money-cost)
		penny = int((float(money-cost)-dollars)*100)
		peny = penny
		cent = 0
		howmuchpenny=[]
		while True:
			if peny ==0:
				break
			if peny>=25:
				for i in range(int(peny/25)):
					howmuchpenny.append(25)
				cent+=int(peny/25)
				peny = peny%25
			elif peny>=10:
				for i in range(int(peny/10)):
					howmuchpenny.append(10)
				cent+=int(peny/10)
				peny=peny%10
			elif peny>=5:
				for i in range(int(peny/5)):
					howmuchpenny.append(5)
				cent+=int(peny/5)
				peny=peny%5
			elif peny>=1:
				for i in range(int(peny/1)):
					howmuchpenny.append(1)
				cent+=int(peny/1)
				peny=peny%1


	return ('{}-dollars, {}-penny, {}-amount of coins, {}'.format(dollars,penny,cent,howmuchpenny))



def main():
	while True:
		cost = input('if you want stop, push: 0\nHow much cost: ')
		if cost == '0':
			break
		money = input('How much money: ')
		start = 0
		cost = cost.replace(',','.')
		money = money.replace(',','.')
		for i in range(len(cost)):
			if ord(cost[i])>57 or ord(cost[i])<=45 or ord(cost[i])==47:
				start+=1
				break
		for i in range(len(money)):
			if ord(money[i])>57 or ord(money[i])<45 or ord(cost[i])==47:
				start+=1
				break
		if start == 0:
			print(compute(cost,money))
		if start!=0:
			print('you must print only numbers!')



		
if __name__ == '__main__':
    main()