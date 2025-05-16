class Solution:
    def myAtoi(self, s: str) -> int:

        sign = ["+", "-", " "]

        # Handles the case when s is empty
        if len(s) == 0 or s in sign:
            return 0

        # Stops when first is non-digit and non sign and non space

        if not s[0].isdigit() and s[0] not in sign:
            return 0

        ans = ""
        hasDigit = 0
        hasSign = 0
        for c in s:
            # Ignore Leading WhiteSpace
            if c == " ":
                if hasDigit == 1:
                    break
                if hasSign == 1:
                    return 0
                continue
            # Checks for Signs
            if c == "-" or c == "+":
                if hasDigit == 1:
                    break
                # Handles the case of +-12
                elif hasSign == 1:
                    return 0
                ###################
                hasSign = 1
                ans = c
                continue
            if c.isdigit():
                ans = ans + c
                if int(ans) > 2147483648 - 1:
                    ans = "2147483647"
                elif int(ans) < -2147483648:
                    ans = "-2147483648"
                hasDigit = 1
                continue
            # Stops if c is non digit and ans already has digit
            if not c.isdigit() and hasDigit == 1:
                break
            if not c.isdigit():
                return 0

        if ans == "":
            return 0
        else:
            return int(ans)
