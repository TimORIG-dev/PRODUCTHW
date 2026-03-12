import random


def _ask_int(prompt: str) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Введите целое число.")


def _ask_yes_no(prompt: str) -> bool:
    while True:
        raw = input(prompt).strip().lower()
        if raw in {"y", "yes", "д", "да"}:
            return True
        if raw in {"n", "no", "н", "нет"}:
            return False
        print("Ответьте 'да' или 'нет' (y/n).")


def play_once(rng: random.Random) -> int:
    secret = rng.randint(1, 100)
    attempts = 0

    print("Я загадал число от 1 до 100. Попробуйте угадать!")
    while True:
        guess = _ask_int("Ваш вариант: ")
        attempts += 1

        if guess < secret:
            print("Больше")
        elif guess > secret:
            print("Меньше")
        else:
            print(f"Угадали! Количество попыток: {attempts}")
            return attempts


def main() -> None:
    rng = random.Random()

    while True:
        play_once(rng)
        if not _ask_yes_no("Сыграть ещё раз? (y/n): "):
            print("Спасибо за игру!")
            return


if __name__ == "__main__":
    main()
