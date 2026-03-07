def find_word_complete(grid, word):
    """
    Find all complete matches of a word (or its reverse) in a 2D grid.
    Allows up to one mismatch per match; wildcards " " and "-" match any letter.
    Returns a list of matches: (row, col, direction, is_reverse, mismatch_index).
    mismatch_index is -1 for exact match, or 0-based index of the mismatched letter.
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
        mismatch_index = -1
        for i in range(len(word_seq)):
            nr, nc = r + dr * i, c + dc * i
            cell = grid[nr][nc] if in_bounds(nr, nc) else None
            if cell is None:
                return None
            if cell == word_seq[i] or cell in (' ', '-'):
                continue
            if mismatch_index >= 0:
                return None
            mismatch_index = i
        return mismatch_index

    for r in range(n_rows):
        for c in range(n_cols):
            for dr, dc, label in directions:
                res = check_direction(r, c, dr, dc, word)
                if res is not None:
                    matches.append((r, c, label, False, res))
                res = check_direction(r, c, dr, dc, word[::-1])
                if res is not None:
                    matches.append((r, c, label, True, res))
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
    r, c, direction, is_reverse, mismatch_index = m
    mismatch_info = f", Mismatch at position {mismatch_index+1}" if mismatch_index >= 0 else ""
    print(f"Start: ({r+1},{c+1}), Direction: {direction}, Reverse: {is_reverse}{mismatch_info}")
