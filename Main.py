import random

def deal_hand(hand):
    while len(hand) != 2:
        hand.append(random.randint(1, 11))
    return hand


print("**********************************************")
print("************  The BlackJack Game  ************")
print("**********************************************\n")

cont = False
player_win_count = 0
computer_win_count = 0

balance = int(input("How much money would you like to bring to the table (minimum $10)? "))
if balance < 10:
    balance = int(input("Minimum balance must be $10! Enter new initial balance: "))

while not cont:

    if balance < 5:
        print("You have lost all your money. Thanks for playing!")
        break

    dealers_hand = []
    deal_hand(dealers_hand)
    print("Dealer Has: ? &", dealers_hand[1])

    players_hand = []
    deal_hand(players_hand)
    print("You Have:", players_hand)

    bet_amount = int(input("How much would you like to bet (minimum $5)? "))
    if bet_amount < 5:
        bet_amount = int(input("Minimum bet amount must be $5! Please enter a new amount: "))
    elif bet_amount > balance:
        print(f"Balance: ${balance}")
        bet_amount = int(input("Enter valid bet amount: "))

    balance = balance - bet_amount

    if sum(dealers_hand) == 21:
        print("Blackjack! Dealer Wins!")
        computer_win_count += 1
        balance = balance - bet_amount
    elif sum(dealers_hand) > 21:
        print("Dealer was a bust!")
        player_win_count += 1

    while sum(players_hand) < 21:
        action = str(input("Do you want to stay or hit (s/h)? "))

        if action.lower() == "h":
            players_hand.append(random.randint(1, 11))
            print("You Have:", players_hand)
            print("Your current total is:", str(sum(players_hand)))

        else:
            print("Dealer Has:", dealers_hand)
            print("Dealer has a total of:", str(sum(dealers_hand)))
            print("You Have:", players_hand)
            print("Your current total is:", str(sum(players_hand)))

            if sum(dealers_hand) > sum(players_hand):
                print("Dealer Wins!")
                computer_win_count += 1
                balance = balance - bet_amount
            else:
                print("You Win!")
                player_win_count += 1
                balance = balance + (2 * bet_amount)
                break

    if sum(players_hand) > 21:
        print("You busted! Dealer Wins!")
        computer_win_count += 1
        balance = balance - bet_amount
    elif sum(players_hand) == 21:
        print("Blackjack! You Win!")
        player_win_count += 1
        balance = balance + (2.5 * bet_amount)

    print(f"Your current balance is: ${balance}")
    wish_to_continue = str(input("Do you wish to play another game (y/n)? "))

    if wish_to_continue.lower() == "n":
        cont = True
        print()
        print(f"Scores: Computer = {computer_win_count} \t Player = {player_win_count}")
        print("Thank you for playing!")
    else:
        print()
