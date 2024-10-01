#
def gcd(a, b):
    max_gcd = 0
    if b > a:
        [a,b] = [b,a]
    for current_num in range(1, b + 1):
        if b % current_num == 0 and a % current_num == 0:
            max_gcd = current_num
        return max_gcd

print(f"gcd is - {gcd(3,8)}")