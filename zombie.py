import random

health = 100
food = 5
days = 1

print("==== ZOMBIE SURVIVAL ====")
print("Survive as long as you can!\n")

while health > 0:

    print("\nDay:", days)
    print("Health:", health)
    print("Food:", food)

    print("\n1. Search")
    print("2. Eat")
    print("3. Rest")
    print("4. Quit")

    choice = input("Choose: ")

    if choice == "1":
        event = random.randint(1, 4)

        if event == 1:
            print("You found 2 food!")
            food += 2

        elif event == 2:
            damage = random.randint(10, 25)
            print("A zombie attacked!")
            print("You lost", damage, "health.")
            health -= damage

        elif event == 3:
            print("You found a medkit!")
            heal = random.randint(10, 20)
            health += heal
            if health > 100:
                health = 100
            print("Recovered", heal, "health.")

        else:
            print("Nothing happened today.")

    elif choice == "2":
        if food > 0:
            food -= 1
            health += 15
            if health > 100:
                health = 100
            print("You ate some food.")
        else:
            print("No food left!")

    elif choice == "3":
        print("You rested.")
        health -= 5
        days += 1

    elif choice == "4":
        print("You gave up...")
        break

    else:
        print("Invalid choice!")

    if random.randint(1, 5) == 1:
        print("A zombie sneaked up on you!")
        health -= 10

    if health <= 0:
        print("\n💀 GAME OVER")
        print("You survived", days, "days.")

print("\nThanks for playing!")