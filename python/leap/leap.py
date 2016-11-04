
def is_leap_year(year):
    if not year:
        return False

    mod4   = year % 4
    mod100 = year % 100
    mod400 = year % 400

    if (mod4==0):
        if (mod100==0):
            if (mod400==0):
                return True

    if (mod4==0) and (mod400==0):
        return True

    return False

if __name__ == '__main__':
    import sys
    result = is_leap_year(int(sys.argv[1]))
    print result
