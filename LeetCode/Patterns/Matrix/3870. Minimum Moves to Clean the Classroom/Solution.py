from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        rows = len(classroom)
        cols = len(classroom[0])

        litter = {}
        start_r = 0
        start_c = 0

        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)
                elif classroom[r][c] == 'S':
                    start_r = r
                    start_c = c

        total = len(litter)
        target = (1 << total) - 1

        q = deque()
        q.append((start_r, start_c, energy, 0))

        visited = set()
        visited.add((start_r, start_c, energy, 0))

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        moves = 0

        while q:
            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == target:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1

                    if ne < 0:
                        continue

                    new_mask = mask

                    if classroom[nr][nc] == 'L':
                        idx = litter[(nr, nc)]
                        new_mask |= (1 << idx)

                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, ne, new_mask)

                    if state in visited:
                        continue

                    visited.add(state)
                    q.append(state)

            moves += 1

        return -1