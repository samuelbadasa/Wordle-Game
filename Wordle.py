from wordle_helper import select_random_word, print_color

def main():
    wordle = select_random_word()
    wordle=wordle.lower()
    for tries in range(6):
        a=input("Enter a guess:")
        for i in range(len(wordle)):
            a=a.lower()
            if a[i]==wordle[i]:
                print_color(a[i],"GREEN")
            elif a[i] in wordle:
                print_color(a[i],"YELLOW")
            else:
                print_color(a[i],"BLACK")
        print()

        if wordle==a:
            print("You got it!")
            break
    if wordle!=a:
        print("Sorry, the word was:",wordle)
main()