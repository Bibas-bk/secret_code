print("***snake,water,gun**")
print("enter s for snake, w for water, g for gun")
snake="s"
gun="g"
water="w"
while True:
  user=input("enter your choice:")
  player=input("enter player choice:")
  if(user==player):
     print("draw")
  elif(user=="s" and player=="w" or user=="w" and player=="g" or user=="g" and player=="s"):

     print("user wins")
  else:
     print("player wins")

