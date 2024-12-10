def get_num_of_cards(cards: list[int], start, end) -> int:
    # No cards to look through
    if (end - start == 0):
        return 0

    total = 0
    for i in range(start, end):
        total += cards[i]

        first = i+1
        last = i+1+cards[i]

        # Add the cards we just got
        total += get_num_of_cards(cards, first, last)

    return total

def main():
    winning_total = 0

    scratch_cards = open("day4.txt", "r").readlines()
    scratch_card_winning_nums = []

    for card in scratch_cards:
        winning_nums = card.split(": ")[1].split(" | ")[0].split()
        card_nums = card.split(": ")[1].split(" | ")[1].split()

        card_worth = 0
        num_of_wins = 0
        for num in card_nums:
            if num in winning_nums:
                num_of_wins += 1
                if card_worth == 0: card_worth = 1
                else: card_worth *= 2

        winning_total += card_worth
        scratch_card_winning_nums.append(num_of_wins)

    print(winning_total)
    num_of_cards = get_num_of_cards(scratch_card_winning_nums, 0, len(scratch_card_winning_nums))
    num_of_cards += len(scratch_cards)
    print(num_of_cards)

if __name__ == "__main__":
    main()