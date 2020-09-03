def get_odd_lines():
    with open("data/queenLyrics.txt") as f:
        odd_lines = []
        for index, line in enumerate(f.readlines()):
            if (index+1)%2==1:
                odd_lines.append(line)
    return odd_lines