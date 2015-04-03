def foobar(n):
    for i in range(n+1):
        if i % 15 == 0:
            print "foo"
        elif i % 5 == 0:
            print "bar"
        elif i % 3 == 0:
            print "foobar"
        else:
            print i

print foobar(20)
