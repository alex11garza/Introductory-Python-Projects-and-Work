#CodeLab 3 Alex Garza, Hector Guerra, Meecah Glas 
#3/2/2023 CS303E
def frame_this(list_of_words):
    max_length = max([len(word) for word in list_of_words] ) + 4
    i = "*" * (max_length + 2)
    print(i)
    for word in list_of_words:
        space_needed = max_length - len(word)
        left_space = space_needed // 2 
        right_space = space_needed - left_space
        x = "*" + " " * left_space + word + " " * right_space + "*"
        print(x)
    print(i)

def get_average(list_of_nums):
    total = 0 
    for y in list_of_nums:
        total += y
    return round(total / len(list_of_nums))

def draw_three(list_of_cards):
    return list_of_cards [:3]

def main():
    my_word = ["Hello", "World", "in","a","frame"]
    my_numbers = [4,5,4,3]
    my_cards = ['2 of Hearts', '6 of Spades', 'Jack of Diamonds', 'Queen of Clubs', 'King of Clubs']

    frame_this(my_word)
    print(get_average(my_numbers))
    print(draw_three(my_cards))

if __name__ == "__main__":
    main()
