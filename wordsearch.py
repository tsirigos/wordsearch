def find_word_complete(grid, word):
    """
    Find all complete matches of a word (or its reverse) in a 2D grid.
    Returns a list of matches with (row, col, direction, is_reverse)
    Directions: 'H' = horizontal, 'V' = vertical, 'D1' = diag top-left→bottom-right, 'D2' = diag top-right→bottom-left
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    word_len = len(word)
    matches = []

    # Define directions: (dr, dc, label)
    directions = [
        (0, 1, 'H'),    # horizontal right
        (1, 0, 'V'),    # vertical down
        (1, 1, 'D1'),   # diagonal down-right
        (1, -1, 'D2')   # diagonal down-left
    ]

    def in_bounds(r, c):
        return 0 <= r < n_rows and 0 <= c < n_cols

    def check_direction(r, c, dr, dc, word_seq):
        for i in range(len(word_seq)):
            nr, nc = r + dr * i, c + dc * i
            if not in_bounds(nr, nc) or grid[nr][nc] != word_seq[i]:
                return False
        return True

    for r in range(n_rows):
        for c in range(n_cols):
            for dr, dc, label in directions:
                # Check forward
                if check_direction(r, c, dr, dc, word):
                    matches.append((r, c, label, False))
                # Check backward
                if check_direction(r, c, dr, dc, word[::-1]):
                    matches.append((r, c, label, True))
    return matches

# Example usage:

grid = [
    list("CSDJSOMALLEMYJDSCDZ"),
    list("MOEEIALGJTETCCEAHEY"),
    list("EEMHDRIOYFUOPODMATZ"),
    list("KSROCOBDEDMTGCOAOSO"),
    list("PTTPSONTSOEEOBNLDUT"),
    list("BLYOEENDEOURCADLHYS"),
    list("BAADYOLSELNLKCEEAAU"),
    list("JGYTFBTLAEBEBPETSNG"),
    list("HOZPEAITANRKUBSOTOO"),
    list("SOLUUUSECMEEMBUMASH"),
    list("WQLSKAQDNGAUSSSOPVC"),
    list("BBTAHADIOSKUBZTCREU"),
    list("SEDRATSANEUBSGELOMM"),
    list("DELGUSTOESMIOTDHNOF"),
    list("GANANAMATSAHUMEETSW"),
    list("RZOJGCOMOESTASCDOWT")
]

word = "COMOESTAUSTED"
matches = find_word_complete(grid, word)

print("Matches found:")
for m in matches:
    r, c, direction, is_reverse = m
    print(f"Start: ({r+1},{c+1}), Direction: {direction}, Reverse: {is_reverse}")
