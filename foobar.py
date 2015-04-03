def foobar(n):
    for i in range(n):
        print i
        if i % 3 == 0:
            print "foo"
        elif i % 5 == 0:
            print "bar"
        elif i % 15 == 0:
            return "foobar"
        else:
            return i

print foobar(20)
