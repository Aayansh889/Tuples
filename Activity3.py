weather=(1,0,0,1,0,1,1,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0)
rangee=len(weather)
rainy=0
sunny=0
for i in range(rangee):
    if weather[i]==1:
        rainy+=1
    else:
        sunny+=1
if sunny>rainy:
    print("Good Weather")
elif sunny==rainy:
    print("Moderate Weather")
else:
    print("Bad Weather")