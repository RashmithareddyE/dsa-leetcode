class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        result = []

        def backtrack(path, used):

            if len(path) == len(s1):
                result.append("".join(path))
                return

            for i in range(len(s1)):

                if used[i]:
                    continue

                path.append(s1[i])
                used[i] = True

                backtrack(path, used)

                path.pop()
                used[i] = False

        backtrack([], [False] * len(s1))
        for p in result:
            if p in s2:
                return True

        return False