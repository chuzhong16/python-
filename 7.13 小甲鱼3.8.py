import random
secret=random.randint(1,10)
temp=input("猜猜是哪个数字")
guess=int(temp)
while guess!=secret:
	temp=input("猜错了请重新输入：")
	guess=int(temp)
	if guess==secret:
		print("猜中了")
	else:
		if guess>secret:
			print("大了")
		else:
			print("小了")
print("游戏结束")