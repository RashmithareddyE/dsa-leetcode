from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        rows = len(classroom)
        cols = len(classroom[0])

        # Give every L an ID
        litter = {}
        start_r = start_c = 0

        for r in range(rows):
            for c in range(cols):
                if classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

                if classroom[r][c] == 'S':
                    start_r = r
                    start_c = c

        total = len(litter)

        # All litter collected
        target = (1 << total) - 1

        # state = (row, col, remaining_energy, collected_mask)
        q = deque()
        q.append((start_r, start_c, energy, 0))

        # visited states
        visited = set()
        visited.add((start_r, start_c, energy, 0))

        directions = [
            (-1, 0),   # up
            (1, 0),    # down
            (0, -1),   # left
            (0, 1)     # right
        ]

        moves = 0

        while q:

            for _ in range(len(q)):

                r, c, e, mask = q.popleft()

                # All litter collected
                if mask == target:
                    return moves

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    # Obstacle
                    if classroom[nr][nc] == 'X':
                        continue

                    # One move costs one energy
                    ne = e - 1

                    if ne < 0:
                        continue

                    new_mask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        idx = litter[(nr, nc)]
                        new_mask |= (1 << idx)

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, ne, new_mask)

                    if state in visited:
                        continue

                    visited.add(state)
                    q.append(state)

            moves += 1

        return -1