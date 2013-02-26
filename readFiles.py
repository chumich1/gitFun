import re

color = open('favoriteColor.txt', "r")
plans = open('plansForWeekend.txt', "r")

a= color.read()
b= plans.read()
d = re.findall(r'(homework)', b)
e = re.sub(r'(homework)', "video games", b)
plans.close()

plans = open('plansForWeekend.txt', "w")
plans.write(e)
plans.close()


