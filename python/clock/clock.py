import string

def Clock(hours=0,minutes=0):
    
    return "%s:%s" % (string.zfill(hours % 24, 2), string.zfill(minutes % 60, 2))

if __name__ == '__main__':
    import sys
    print Clock(int(sys.argv[1]), int(sys.argv[2]))
