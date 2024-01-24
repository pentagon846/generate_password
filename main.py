import random


def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+"
    password = ''.join(random.choice(characters) for _ in range(length))
    with open('password.txt', 'a') as file:
        file.write(password + '\n')
    return password


generated_password = generate_password(16)
print(generated_password)
