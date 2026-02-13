def checkmate(board):

    rows = board.strip().split("\n")
    n = len(rows)

    # เช็คสี่เหลี่ยม
    for row in rows:
        if len(row) != n:
            print("Error")
            return
        
    # นับจำนวนหมาก
    countK = 0
    countQ = 0
    countR = 0
    countB = 0
    countP = 0

    grid = []

    special = False

    for r in range(n):
        temp = []
        for c in range(n):
            ch = rows[r][c]

            if ch == "K":
                countK += 1
            elif ch == "Q":
                countQ += 1
            elif ch == "R":
                countR += 1
            elif ch == "B":
                countB += 1
            elif ch == "P":
                countP += 1
            elif ch == ".":
                pass
            else:
                special = True
                ch = "."

            temp.append(ch)

        grid.append(temp)

    # จำกัดจำนวน (if แยกทีละตัว)
    if countK != 1:
        print("King มีเกินจำนวน 1 ตัว")
        return

    if countQ > 1:
        print("Queen มีเกินจำนวน 1 ตัว")
        return

    if countR > 2:
        print("Rook มีเกินจำนวน 2 ตัว")
        return

    if countB > 2:
        print("Bishop มีเกินจำนวน 2 ตัว")
        return

    if countP > 8:
        print("Pawn มีเกินจำนวน 8 ตัว")
        return

    # หา King
    kr = -1
    kc = -1

    for r in range(n):
        for c in range(n):
            if grid[r][c] == "K":
                kr = r
                kc = c

    # เช็คการโจมตี
    for r in range(n):
        for c in range(n):

            piece = grid[r][c]

            if piece == "." or piece == "K":
                continue

            # Pawn
            if piece == "P":
                if r-1 == kr and c-1 == kc:
                    print("Success"); return
                if r-1 == kr and c+1 == kc:
                    print("Success"); return
                
            # Bishop
            if piece == "B":
                for dr, dc in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                    nr = r
                    nc = c
                    while 0 <= nr+dr < n and 0 <= nc+dc < n:
                        nr += dr
                        nc += dc
                        if grid[nr][nc] != ".":
                            if nr == kr and nc == kc:
                                print("Success"); return
                            break

            # Rook
            if piece == "R":
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr = r
                    nc = c
                    while 0 <= nr+dr < n and 0 <= nc+dc < n:
                        nr += dr
                        nc += dc
                        if grid[nr][nc] != ".":
                            if nr == kr and nc == kc:
                                print("Success"); return
                            break
                        
            # Queen
            if piece == "Q":
                for dr, dc in [
                    (-1,-1),(-1,1),(1,-1),(1,1),
                    (-1,0),(1,0),(0,-1),(0,1)
                ]:
                    nr = r
                    nc = c
                    while 0 <= nr+dr < n and 0 <= nc+dc < n:
                        nr += dr
                        nc += dc
                        if grid[nr][nc] != ".":
                            if nr == kr and nc == kc:
                                print("Success"); return
                            break

    print("Fail")
