import random

def game_tebak_angka():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Tebak angka (1-100): "))
        attempts += 1

        if guess < secret_number:
            print("Terlalu rendah, coba lagi!")
        elif guess > secret_number:
            print("Terlalu tinggi, coba lagi!")
        else:
            print("Selamat! Angka yang Anda tebak benar.")
            print("Anda berhasil menebak dalam {} percobaan.".format(attempts))
            break

def main():
    print("=== Game Tebak Angka ===")
    print("Saya telah memilih angka antara 1 hingga 100.")
    print("Coba tebak angka yang saya pilih.")
    print("========================")

    while True:
        game_tebak_angka()
        play_again = input("Ingin bermain lagi? (y/n): ")
        if play_again.lower() != 'y':
            break

    print("Terima kasih telah bermain!")

if __name__ == '__main__':
    main()
