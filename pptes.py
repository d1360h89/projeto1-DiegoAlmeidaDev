import random

while True:
    # Código anterior aqui
    user_choice = input('Escolha (pedra, papel ou tesoura): ')

    choices = ["pedra","papel","tesoura"]
    computer_choice = random.choice(choices)   

    if user_choice == computer_choice:
        print("Empate!")
    elif (user_choice == "pedra" and computer_choice == "tesoura") or (user_choice == "papel" and computer_choice == "pedra") or (user_choice == "tesoura" and computer_choice == "papel"):
        print("Você venceu!")
    else:
        print("O computador venceu!")
    play_again = input("Quer jogar novamente? (s/n): ")
    if play_again.lower() != "s":
        break
