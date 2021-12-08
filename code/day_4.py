#%% Part 1 ---------------------------------------------------------------------


def get_file(filepath):
    with open(filepath) as f:
        data = f.readlines()
        data = [x.rstrip() for x in data]
    return data


def get_calls_and_boards(data):
    calls = []
    all_boards = []
    board = []
    for d in data:
        # Determine Length of line
        if len(d) == 0:
            if len(board) == 0:
                continue
            else:
                all_boards.append(board)
                board = []
        elif len(d) == 14:
            board.append(d.split())
        elif len(d) > 50:
            calls.extend(d.split(","))
    # Append the last board
    all_boards.append(board)
    return calls, all_boards


# Marking function
def mark_boards(call, to_mark):
    # Iterate over lists and replace call number with 'X'
    for i in range(len(to_mark)):  # Get index of each board
        for b in range(len(to_mark[i])):  # get index of each row
            for n in range(len(to_mark[i][b])):  # get index of each element
                if call == to_mark[i][b][n]:  # Check if value matches call
                    to_mark[i][b][n] = "X"  # reassign if it does
    return call, to_mark  # Return marked boards


def check_for_winner(boards):
    winner = False
    loop = 0
    while winner == False:
        if loop == len(boards) - 1:
            break
        # Get a card and check the rows
        for i in range(len(boards)):
            for b in range(len(boards[i])):
                # Horizontal Check
                if boards[i][b] == list(["X", "X", "X", "X", "X"]):
                    winner == True
                    return i
                # Vertical Check
                v_list = []
                for j in range(0, 5):
                    v_list.extend(boards[i][j][b])
                if v_list == list(["X", "X", "X", "X", "X"]):
                    winner == True
                    return i
        loop += 1
    if winner == True:
        return i
    else:
        return "No winner"


def mark_and_check(calls, boards):
    for call in calls:
        last_call, boards = mark_boards(call, boards)
        card = check_for_winner(boards)
        if card == "No winner":
            continue
        else:
            print("Winner!!!")
            break
    return card, boards, last_call


def score_card(card, last_call):
    score = 0
    for row in card:
        for item in row:
            try:
                score += int(item)
            except:
                pass
    return score * int(last_call)


def main():
    data = get_file("../data/day_4_data.txt")
    calls, boards = get_calls_and_boards(data)
    winner_id, ending_boards, last_call = mark_and_check(calls, boards)
    winner = ending_boards[winner_id]
    final_score = score_card(winner, last_call)
    for row in winner:
        print(row)
    print(f"Final Score: {final_score}")


if __name__ == "__main__":
    main()

# %%
