from replit import clear
from art import logo
import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
stop_game=True

def draw_card(user_cards,dealer_cards,user_sum,dealer_sum):
  
    if isBust(user_sum):
      if user_cards[-1]==11:
        user_cards[-1]=1
        user_sum+=1
        if isBust(user_sum):
          print(f"your cards{user_cards}, your score is>21")
          print("Dealer Wins!")
          
      else:
        print(f"your cards{user_cards}, your score is>21")
        print("Dealer Wins!")

    else:
      print(f"Your cards are {user_cards}, your current score is {user_sum}")
      print(f"Dealer has {dealer_cards[0]}")
      ans_drawcard=input("do you need a card: type 'y' or 'n' ")
      if ans_drawcard=="y":
        user_cards.append(cards[random.randint(0,12)])
        user_sum+=user_cards[-1]
        return draw_card(user_cards,dealer_cards,user_sum,dealer_sum)
      else:
        
        return user_sum,dealer_sum
def isBust(sumOfCards):
  if sumOfCards>21:
    return True
  else:
    return False

while stop_game==True:
  wantToPlay=input("Do you want to play black jack: type 'y' or 'n' ")
  if wantToPlay=='y':
    clear()
    print(logo)
    user_sum=0
    dealer_sum=0
    user_cards=[]
    dealer_cards=[]
    user_cards.append(cards[random.randint(0,12)])
    user_cards.append(cards[random.randint(0,12)])
    dealer_cards.append(cards[random.randint(0,12)])
    dealer_cards.append(cards[random.randint(0,12)])
    user_sum=0
    dealer_sum=0
    for card in user_cards:
      user_sum+=card

    for card in dealer_cards:
      dealer_sum+=card

    if dealer_sum==21:
      print(f"dealer has {dealer_cards}, Dealer Wins!")

    elif user_sum==21:
      print(f"you have {user_cards},your score is {user_sum}")
      print(f"computer has {dealer_cards},dealer's score is {dealer_sum}")
      print("You Win!")
    user_sum,dealer_sum=draw_card(user_cards,dealer_cards,user_sum,dealer_sum)
    while (dealer_sum<17):
      dealer_cards.append(cards[random.randint(0,12)])
      if dealer_cards[-1]==11:
        dealer_cards[-1]=1
      dealer_sum+=dealer_cards[-1]
    if dealer_sum>21:
      print(f"Dealer's cards are {dealer_cards},Dealer's score {dealer_sum}")
      print("You Win!")
    else:
      if user_sum>dealer_sum:
        print(f"Dealer's cards are {dealer_cards},Dealer's score {dealer_sum}")
        print("You Win!")
      elif user_sum==dealer_sum:
        print(f"Dealer's cards are {dealer_cards},Dealer's score {dealer_sum}")
        print('Draw')
      else:
        print(f"Dealer's cards are {dealer_cards},Dealer's score {dealer_sum}")
        print("Dealer Wins!")
  else:
    stop_game=False
