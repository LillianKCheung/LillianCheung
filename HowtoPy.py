import random
from wonderwords import RandomWord
mad_lib=RandomWord()
#this is an example of how to round and answer.
"""
equation=round((4.5*734+127/49),3)
print(equation)
eqround2=round(equation,2)
print(eqround2)
#how to exponant : 2**3 = 8

#Example of powers
SixSqQuilt=6 ** 2
print(SixSqQuilt)
#modulo operator % is a round that has issues cause it cuts shit off.

#magic 8 ball: how to use random import random .radint()
name="Lillian"
question= "Will I finish this assignment without help? " + "\n"
random_number=random.randint(1,13)
if name=="":
  print (question + "Magic 8-Ball's answers: Outlook not so good" )
elif question== "":
  print("You must ask a question to know the future.")
else:
  print(name + " asks: " + question + "Magic 8-Ball's answers: " )
  if str(random_number) == "1" :
    print("Yes - definitely!")
  elif str(random_number) == "2":
    print("It is decidedly so!")
  elif str(random_number) == "3":
    print("Without a doubt!")
  elif str(random_number)== "4":
    print("Reply hazy, try again.")
  elif str(random_number) == "5":
    print("Ask again later!")
  elif str(random_number) == "6":
    print("Better not tell you now.")
  elif str(random_number) == "7":
    print("My sources say no.")
  elif str(random_number) == "8":
    print ("Outlook not so good!")
  elif str(random_number) == "9":
    print("Very doubtful!")
  elif str(random_number) == "10":
    print("Today will end in tears.")
  elif str(random_number) == "11":
    print("Today will be a day you always remember.")
  elif str(random_number) == "12":
    print("I have faith, you have what it takes to win.")
  elif str(random_number) == "13":
    print("Keep trying, you will win eventually.")
  else :
    print("Error")

    #This is a discussion about how to use type errors.
import math

    # area of a triangle
base = 20
height = 30
Area = base * height * 0.5

print("The Triangle Area is : ", Area)

    # area of a rectangle
l = 2
w = 12
Area = l * w

print("The Rectangle Area is : ", Area)

    # Area of a circle
radius = 36
Area = math.pi * radius ** 2

print("The Circle Area is : ", round(Area, 2))
# can use a comma instead of a + to add a string and int together

#Lists (how to append and remove)
orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
print(orders)
new_flowers=["roses", "morning glories"]
combined_flowers=orders+new_flowers
print(combined_flowers)
print(new_flowers[1])
print(new_flowers[-1])#this is coming at the end of the list from the bottom up
new_flowers[0]="Gardenia"
print(new_flowers)
#list 2D
family_ages=[["mom",65],["dad",68],["bro",41],["sis",40],["me",38],]
family_ages.append(["ChiHo",40]) #this method will only append one type of list at any one time.
family_ages.append(["Maggie",38])
family_ages.append(["Richie",41])
print(family_ages)
#2d going through an array
print(family_ages[4][0])
print(family_ages[-1][-2])
#using the negative numbers we can go backwards to get data out of a 2D array.
married_details=[["Lillian",38,"blue eyes"],["Eric",40,"blue eyes"]]
married_details[1][2]="brown eyes"
print(married_details)
#indexing through array
preferred_size=["Small","Large","Medium"]
preferred_size.append("Medium")
print(preferred_size) # differences to the list
#REMOVEAL FROM A 2D ARRAY
customer_data=[["Ainsley","Small",True],["Ben","Large",False],["Chani","Medium",True],["Depak","Medium",False]]
print(customer_data)
customer_data[2][2]=False
customer_data[1].remove(False)
print(customer_data)
# use verb=zip(item1,item2) then verb2=list(verb) to combine two lists into one and make it an imutable tuple.
#FOR LOOPS EXAMPLES AND INSTRUCTIONS!
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
index=0
for age in ages:
  if age < 21:
    continue
  print(age) # continue is inside the if statement and printing happens one tab over from this , this will skip the
  #peramitor you do not want to keep or print.
  sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
  scoops_sold = 0
  for location in sales_data:
    print(location)
    for scoops in location:
      scoops_sold += scoops
  print(scoops_sold)
  #in order to add the sums of a list make sure and look at scoops and scoops_sold for how to add in a for loop.
  grades = [90, 88, 62, 76, 74, 89, 48, 57]
  #this is filling a list WITH A FOR LOOP THAT IS BEING CHANGED AND FILLED AT THE SAME TIME. 
  scaled_grades = [grade + 12 for grade in grades]
  scaled_grades.sort(reverse=True)
  print(scaled_grades) #fucking awesome example of creating a list and a for loop inside of a list.
  THIS IS ANOTHER EXAMPLE OF FOR LOOPS INSIDE OF A LIST
single_digits=[0,1,2,3,4,5,6,7,8,9]
squares=[single**2 for single in single_digits]
print(squares)
cubes=[single**3 for single in single_digits]
print(cubes)
  # this is adding to a list and using an if statement
  heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
  can_ride_coaster = []
  for height in heights:
    if height <= 161:
      continue
    can_ride_coaster.append(height)
  print(can_ride_coaster)
  PROJECT EXAMPLE OF LOOPS AND LIST 
  hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price=0
total_revenue=0
for price in prices:  
  total_price+=price

print(total_price)
avg=len(prices)
print(avg)
average_price=total_price/avg
print(average_price)
new_prices=[price-5 for price in prices]
print(new_prices)
for i in range (8):
  total_revenue+=prices[i]*last_week[i]
print(total_revenue)
average_daily_revenue=total_revenue/7
print(average_daily_revenue)
cuts_under_thirty=[]
for i in range (len(new_prices)):
  cuts_under_thirty+=[hairstyles[i],prices[i]]
print(cuts_under_thirty)
  """
adverbs = ["abnormally", " absentmindedly", " accidentally", " acidly", " actually", " adventurously", " afterwards",
         " almost", " always", " angrily", " annually", " anxiously", " arrogantly", " awkwardly", "badly",
         " bashfully", " beautifully", " bitterly", " bleakly", " blindly",
         " blissfully", " boastfully", "boldly", " bravely", " briefly", " brightly", " briskly", " broadly", " busily",
         "calmly", " carefully", " carelessly", " cautiously", " certainly", " cheerfully", " clearly", " cleverly",
         "closely", " coaxingly", " colorfully", " commonly", " continually", " coolly", " correctly", "courageously",
         "crossly", " cruelly", " curiously",
         "daily", "daintily", "dearly", "deceivingly", "delightfully", "deeply", "defiantly", "deliberately",
         "delightfully", "diligently", "dimly", "doubtfully", "dreamily", "easily", "elegantly", "energetically",
         " enormously", " enthusiastically", " equally", " especially", " even", " evenly", " eventually",
         "exactly", " excitedly", " extremely", "fairly", " faithfully", " famously", " far", " fast", " fatally",
         " ferociously", " fervently", " fiercely", "fondly", " foolishly", " fortunately", " frankly", " frantically",
         " freely", " frenetically",
         "frightfully", " fully", " furiously", "generally", " generously", " gently", " gladly", " gleefully",
         " gracefully", " gratefully", " greatly", "greedily", " happily", " hastily", " healthily", " heavily",
         " helpfully", " helplessly", " highly",
         "honestly", " hopelessly", " hourly", " hungrily", "immediately", " innocently", " inquisitively",
         " instantly", " intensely", " intently", " interestingly", "inwardly", " irritably", " jaggedly", " jealously",
         " joshingly", " joyfully", " joyously", " jovially",
         "jubilantly", " judgmentally", "justly", "keenly", " kiddingly", " kindheartedly", " kindly", " knavishly",
         " knottily", " knowingly", "knowledgeably", " kookily", " lazily", " less", " lightly", " likely", " limply",
         " lively", " loftily", " longingly", "loosely", " lovingly", " loudly", " loyally",
         "madly", " majestically", " meaningfully", " mechanically", " merrily", " miserably", " mockingly", "monthly",
         " more", " mortally", " mostly", " mysteriously", " naturally", " nearly", " neatly", " needily", "nervously",
         " never", " nicely", " noisily",
         "obediently", " obnoxiously", " oddly", " offensively", " officially", " often", " only", " openly",
         "optimistically", " overconfidently", " owlishly", "painfully", " partially", " patiently", " perfectly",
         " physically", " playfully", " politely", " poorly",
         "positively", " potentially", " powerfully", " promptly", " properly", " punctually", "quaintly",
         "quarrelsomely", " queasily", " queerly", " questionably", " questioningly", "quicker", "quickly", " quietly",
         " quirkily", " quizzically", "rapidly", " rarely", " readily", " really", " reassuringly", " recklessly",
         " regularly", " reluctantly",
         "repeatedly", " reproachfully", " restfully", " righteously", " rightfully", " rigidly", " roughly", "rudely",
         "sadly", " safely", " scarcely", " scarily", " searchingly", " sedately", " seemingly", " seldom",
         " selfishly", " separately", " seriously", " shakily", " sharply", " sheepishly", " shrilly", " shyly",
         " silently",
         "sleepily", " slowly", " smoothly", " softly", " solemnly", " solidly", " sometimes", " soon", " speedily",
         "stealthily", " sternly", " strictly", " successfully", " suddenly", " surprisingly", " suspiciously",
         " sweetly", " swiftly", " sympathetically",
         "tenderly", " tensely", " terribly", " thankfully", " thoroughly", " thoughtfully", " tightly", " tomorrow",
         "too", " tremendously", " triumphantly", " truly", " truthfully", "ultimately", " unabashedly",
         " unaccountably", " unbearably", " unethically", " unexpectedly",
         "unfortunately", "unimpressively", " unnaturally", " unnecessarily", " utterly", " upbeat", " upliftingly",
         " upright", "upsidedown", " upward", " upwardly", " urgently", "usefully", " uselessly", " usually",
         " utterly",
         "vacantly", " vaguely", " vainly", " valiantly", " vastly", " verbally", " very", " viciously", "victoriously",
         " violently", " vivaciously", "voluntarily", "warmly", " weakly", " wearily", " well", " wetly", " wholly",
         " wildly", " willfully", " wisely", " woefully", " wonderfully", " worriedly", " wrongly",
         "yawningly", " yearly", " yearningly", " yesterday", " yieldingly", " youthfully", "zealously", " zestfully",
         "zestily"]

  #random name generator
  #ucverb, lcverb, ucadvrb, lcadvrb, objct, adjctv, sbjct, auxlry, ttlobj
#def title (adjctv, lcadvrb, ttlobj):
for name in range(10):
  radvb = random.randint(0, 329)
  adj=mad_lib.word(include_parts_of_speech=["adjectives"])
  noun = mad_lib.word(include_parts_of_speech=["noun"])
  adverb=adverbs[radvb]
  print(adverb+ " " +adj+ " " + noun)


