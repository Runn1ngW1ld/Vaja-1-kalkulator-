x = int(raw_input("Vpisi prvo stevilo:"))
print x
y = int(raw_input("Vpisi drugo stevilo:"))
print y
operation = raw_input("+, -, *, /:")
print operation

if operation == "+":
    print x+y

if operation == "-":
    print x-y

if operation == "*":
    print x*y

if operation == "/":
    print float(x)/float(y)
