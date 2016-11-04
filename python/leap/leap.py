
def is_leap_year(year):
    if not year:
        return False

    if (year % 4) == 0 and (year % 100) != 0 or (year % 400 == 0):
        return True
    else: 
        return False

if __name__ == '__main__':
    import sys
    print is_leap_year(int(sys.argv[1]))
