import time

def speed_typing_test():
    
    prompt = "The quick brown fox jumps over the lazy dog."

    print("Welcome to the Speed Typing Test!")
    print("Type the following sentence:\n")
    print(prompt + "\n")

    input("Press Enter to start...")

    start_time = time.time()

    user_input = input()

    end_time = time.time()

    elapsed_time = end_time - start_time
    words_typed = len(user_input.split())
    typing_speed = words_typed / elapsed_time
    accuracy = calculate_accuracy(prompt, user_input)

    print("\n--- Result ---")
    print("Time taken:", elapsed_time, "seconds")
    print("Words typed:", words_typed)
    print("Typing speed:", typing_speed, "words per second")
    print("Accuracy:", accuracy, "%")

def calculate_accuracy(prompt, user_input):
    
    prompt_words = prompt.split()
    user_words = user_input.split()

    if len(prompt_words) != len(user_words):
        return 0

    correct_words = 0
    for prompt_word, user_word in zip(prompt_words, user_words):
        if prompt_word == user_word:
            correct_words += 1

    accuracy = (correct_words / len(prompt_words)) * 100
    return round(accuracy, 2)


speed_typing_test()
