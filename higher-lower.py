import logos
import os 
celebrites = [{"Name":"Justin Timberlake","Occupation":"Music and Actor","Location":"United States", "searchAmount":5500},
          {"Name":"Gigi Hadid","Occupation":"Model","Location":"United States", "searchAmount":2500},
          {"Name":"Maluma","Occupation":"Musicion","Location":"Columbia", "searchAmount":8700},
          {"Name":"Instagram","Occupation":"Social Media Platform","Location":" United States", "searchAmount":9400},
          {"Name":"Selena Gomez","Occupation":"Musicion and Actress","Location":"United States", "searchAmount":1500},
          {"Name":"Miley Cyrus","Occupation":"Musicion","Location":"Columbia", "searchAmount":3200},
          {"Name":"Ariana Grande","Occupation":"Musicion and Actress","Location":"United States", "searchAmount":1800},
          {"Name":"Khloe Kardashian","Occupation":"Reality TV personality and businesswoman","Location":"Columbia", "searchAmount":1200},
          {"Name":"Nicki Minaj","Occupation":"Musicion","Location":"Trinidad and Tobago", "searchAmount":12000},
          {"Name":"David Bekham","Occupation":"Footballer","Location":"United Kingdom", "searchAmount":4600},
          {"Name":"UEFA Champion League","Occupation":"a Club football competition","Location":"Europe", "searchAmount":2200},
          {"Name":"9GAG","Occupation":"a Social Media Platform","Location":"China", "searchAmount":900},
          {"Name":"Shakira","Occupation":"a Musicion","Location":"Columbia", "searchAmount":45000},
          {"Name":"Justin Beiber","Occupation":"a Musicion","Location":"Canada","searchAmount":2800}]
score = 0
# creating second celebrity list
secondListCelebrityList = celebrites.copy()
# removing first element from the second celebrity list
for index in range(len(secondListCelebrityList)):
   if secondListCelebrityList[index]['Name'] == "Justin Timberlake":
      del secondListCelebrityList[index]
      break
num = 0
# appending another value to the list, so it does not get index out of bound error
secondListCelebrityList.append({"Name":"Justin Timberlake","Occupation":"Music and Actor","Location":"United States", "searchAmount":5500})
# looping over both list
print(logos.higherlower)
for celebrity in celebrites:
    secondListCelebrityList[num]
    Name = celebrity['Name']
    Occupation = celebrity['Occupation']
    Location = celebrity["Location"]
    SearchAmount = celebrity["searchAmount"]
    secondName = secondListCelebrityList[num]["Name"]
    secondOccupation = secondListCelebrityList[num]["Occupation"]
    secondLocation = secondListCelebrityList[num]["Location"]
    secondSearchAmount = secondListCelebrityList[num]["searchAmount"]
    print(f"Compare A: {Name}, {Occupation}, from {Location}")
    print(logos.VS)
    print(f"Against B: {secondName}, {secondOccupation}, from {secondLocation} ")
    makeAChoice = input("Who has more followers? type 'A' or 'B'")
    if makeAChoice.lower() == "a":
       if SearchAmount > secondSearchAmount:
          score = score + 1
          print(f"Your right! current score {score}")
       elif SearchAmount < secondSearchAmount:
          print(f"Sorry, that wrong. Final score {score}")
          break
    elif makeAChoice.lower() == "b":
       if SearchAmount < secondSearchAmount:
          score = score + 1
          print(f"Your right! current score {score}")
       elif SearchAmount > secondSearchAmount:
          print(f"Sorry, that wrong. Final score {score}")
          break
    num = num + 1
