class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count1 = [0] * 26
        count2 = [0] * 26

        # Frequency of s1
        for c in s1:
            count1[ord(c) - ord('a')] += 1

        left = 0

        for right in range(len(s2)):

            # Add s2[right]
            count2[ord(s2[right]) - ord('a')] += 1

            # Keep window size equal to s1
            if right - left + 1 > len(s1):
                count2[ord(s2[left]) - ord('a')] -= 1
                left += 1

            # Check frequency match
            if count1 == count2:
                return True

        return False