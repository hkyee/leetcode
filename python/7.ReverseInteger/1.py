class Solution:
    def reverse(self, x: int) -> int:

        ans = ""
        string = str(abs(x))
        # Check for negative, if negative, add a "-" infront of string numbers
        if x < 0:
            ans = "-" + string[::-1]
        else:
            ans = string[::-1]

        # Check for answer within 32 bit range
        # 2^31 =   2147483648
        if int(ans) > (2147483648 - 1) or int(ans) < -2147483648:
            return 0
        else:
            return int(ans)
