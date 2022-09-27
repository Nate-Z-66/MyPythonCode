#add all even numbers utl 1000

result = 0

i = 0

while i <= 1000:

# if its even#
    if i % 2 == 0:
        print(i)
        result = i + result


    i = i + 1

print("total = %d" % result)
