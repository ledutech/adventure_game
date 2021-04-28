import time
import random

mother = ["Mother Goddess of Compassion, Green Tara",
          "Mother Goddess of Protection from Illness, Orange Tara",
          "Mother Goddess of Protection from Fear, Black Wrathful Tara"]
the_mother = random.choice(mother)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(.25)


def valid_input(prompt, option):
    while True:
        response = input(prompt).lower()
        if response in option:
            return response
        else:
            print_pause("Choose a valid destination from the transport list.")


def encounter():
    print_pause("You are on a hike,\n"
                "in search of spiritual awakening\n"
                "high in the Himalayan Mountains.\n")
    print_pause("Surrounded by wispy clouds, you\n"
                "encounter a hidden temple emerging from\n"
                "a nearby snow bank.\n ")
    print_pause("The temple is glittering and radiates with "
                "peacefulness.\n")
    print_pause("Its magnificent stairway "
                "invites you... \n")
    print_pause("...but you SUDDENLY REALIZE...\n")
    print_pause("that your wide-mouth canteen is empty\n"
                "and your gear is down at basecamp.\n")
    print_pause("Gasp!\n ")
    print_pause("You DO HAVE your hand-held transporter.\n"
                "But you definitely NEED a survival strategy!\n")


def temple(offerings):
    print_pause("You ascend the jewel-toned temple steps "
                "and enter the ancient structure.\n ")
    if len(offerings) == 3:
        print_pause("You've harnessed the elements and WON by surviving!\n")
        hike_again()
    else:
        if "fire" in offerings:
            print_pause("You light the sacred fire with your camp lighter.")
            print_pause("The sacred fire illuminates the temple.\n")
            print_pause("You're ready to move out!\n")
            print_pause("Ready for transport?\n ")
            adventure(offerings)
        if "abhaya" in offerings:
            print_pause("You hear a kind voice say:\n")
            print_pause("Go now, harness the elements "
                        "with the Mother's blessing.\n")
            print_pause("You go out and down the temple stairs again.\n")
            print_pause("Ready for transport?\n ")
            adventure(offerings)
        else:
            print_pause("Inside you find a beautiful murti, "
                        "an enormous golden statue of the ")
            print_pause(the_mother)
            print_pause("She looks SO alive, but the temple is freezing.\n ")
            print_pause("The sacred dhune fire has long been extinguished.\n ")
            print_pause("Brrrr!!!!!\n ")
            print_pause("Standing in front of the Goddess, you notice "
                        "a small table before her.\n ")
            print_pause("You realize that it is meant for visitors to "
                        "leave their offerings.\n")
            print_pause("You think you have nothing to give,\n ")
            print_pause("so you go out and down the temple stairs.\n ")
            offerings.append("abhaya")
            adventure(offerings)


def basecamp(offerings):
    print_pause("You lie down on your back in the snow and roll into "
                "a tight ball.\n ")
    if "fire" in offerings:
        print_pause("Wait!  There's nowhere to roll to now.\n ")
        print_pause("You've already got your gear and your transporter.\n ")
        if "abhaya" in offerings:
            print_pause("No broken bones!  Must be the blessing!\n ")
        else:
            print_pause("Ready for transport?\n ")
            adventure(offerings)
        if "water" in offerings:
            print_pause("Your canteen is brimming, let's move out!\n ")
        else:
            print_pause("Ready for transport?\n ")
            adventure(offerings)
    else:
        print_pause("You secure your goggles, cinch "
                    "down the strap on your hat "
                    "and roll down the mountain.\n ")
        print_pause("You are like a human sled! Banzai!\n ")
        print_pause("You land down at basecamp in a crumpled heap.\n ")
        print_pause("Ouch!\n ")
        print_pause("You grab your forgotten survival gear.\n ")
        offerings.append("fire")
    print_pause("Ready for transport?\n ")
    adventure(offerings)


def snowbank(offerings):
    print_pause("You lie down on your back on the snow bank.\n ")
    if "fire" in offerings:
        print_pause("You've got fire!\n ")
    if "water" in offerings:
        print_pause("You've got water, it's time to move out!\n ")
    else:
        print_pause("You start vigorously moving your legs "
                    "in and out and your arms up and down.\n")
        print_pause("A mound of excess snow piles up from your movements, "
                    "which you scoop into your wide-mouth canteen.\n ")
        print_pause("The shallow impression of an angel is "
                    "left behind in the snow.\n")
        print_pause("Hallelujah!\n")
        print_pause("Your canteen will soon be filled "
                    "with melted snow water.\n")
        print_pause("Ready for transport?\n")
        if "fire" not in offerings:
            print_pause("You still need fire.\n")
        offerings.append("water")
    adventure(offerings)


def adventure(offerings):
    print_pause("Please enter the destination number "
                "so your transporter can take you there: ")
    do_next = valid_input("1. Enter the Temple\n"
                          "2. Go down to Basecamp\n"
                          "3. Lie down on the Snow Bank\n",
                          ["1", "2", "3"])
    if do_next == '1':
        temple(offerings)
    elif do_next == '2':
        basecamp(offerings)
    elif do_next == '3':
        snowbank(offerings)


def hike_again():
    response = valid_input("Would you like to hike again? "
                           "Please say 'yes' or 'no'.\n",
                           ["yes", "no"])
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("Very good, initiate transport.")
        play_game()


def play_game():
    offerings = []
    encounter()
    adventure(offerings)
    hike_again()


def play_again():
    option = valid_input("Play again? [y|n]", ['y', 'n'])
    if option in 'y':
        return True
    return False


def game():
    # Infinite loop.
    while True:
        # Play the game in each cycle
        play_game()
        # The stop condition.
        if not play_again():
            print('Bye!')
            exit(0)


if __name__ == '__main__':
    game()
