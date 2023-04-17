print("let's do more elif tasks ")
print("Lets build a sorry recommendation results ")
print("tell us your feelings in regards to this list: sad, happy , mad , angry, sorry and at the end dont forget to tell us where you would like to be helped and what you think should be done to help you : \n choose your comfort in this list { pampered, begged, affection, fixed} ")
action = input("/03[30How are you feeling today ?")
comfort = input("how would you like to be comforted today ?")
if action == "sad":
  print("why are you sad ? and what can be done to help you overcome this feeling?")
  comf =input("how would you like to be assisted ?")
  if comf == "pampered":
    print("dont worry for you are about to be pampered in the best way possible")
  else:
    print("no matter the situation, you got all this under control friend")
elif action == "happy":
  comf = input("how would you like to be ccomforted today ?")
  if comf == "begged":
    print("cheer up friend, life's too short for you to worrry , you got this under control")
  else:
    print(comf,"will be sent to see how helping you is possible ")
    say = input("say okay! so that you would not worry too much anymore ")
    if say == "Okay":
      print("Exactly! you ara all nothing but a champion ")
      print("cheer up buddy, life's exterminated from coding failures")
    else: 
        print("what more do you think can be of help to you ")
elif action == "mad":
    print("only bulls get mad, cmon chop chop ! youre not a bull ")
elif action == "angry":
  anger =input("why are you angry ?")
  print(anger,"will be sent to milugo geofrey to see how you can be helped")
else:
  print("i'm not mad ! i think im slowly becoming a taurus")
what =input("have you find the assistnce you were in search for by going through this code ?")
print(what,"will be sent as your final feelings for this ai")
comment = input("what do you think of this feeling AI ?")
print(comment,"also will be sent to the developer to see if necessary modifications are possible ")