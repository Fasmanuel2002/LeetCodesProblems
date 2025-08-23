class Solution(object):
    def subtractProductAndSum(self, n):
        sum = 0
        multiplication = 1
        while n != 0:
            last = n % 10
            multiplication *= last
            sum += last
            n = n //  10
        rest = multiplication - sum

        return rest
        