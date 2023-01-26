count = 0
distance = 10000
firstFriendSpeed = 1
secondFriendSpeed = 2
dogSpeed = 5
friend = 2
while (distance > 10):
    if (friend == 1):
        time = distance / (dogSpeed - firstFriendSpeed)
        friend = 2
    else:
        time = distance / (secondFriendSpeed + dogSpeed)
        friend = 1
    distance = distance - (secondFriendSpeed - firstFriendSpeed) * time
    count = count + 1
print (count)