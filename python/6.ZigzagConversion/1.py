class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # 0. A  G
        # 1. B FH
        # 2. CE I
        # 3. D  J

        # We simply create a variable d to switch directions
        # Down = 1
        # Up = -1

        # idx = element id (0,1,2....)
        idx = 0
        rows = [[] for _ in range(numRows)]

        if numRows == 1 or len(s) <= numRows:
            return s

        for c in s:
            # Add the element to the correct row
            rows[idx].append(c)
            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1
            idx += d

        for i in range(numRows):
            rows[i] = "".join(rows[i])

        return "".join(rows)
