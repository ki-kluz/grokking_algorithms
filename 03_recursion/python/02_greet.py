def greet2(name):
    print("how are you, ", name, "?", sep='')

def bye():
    print("ok bye!")

def greet(name):
    print("hello, ", name, "!", sep='')
    greet2(name)
    print("getting ready to say bye...")
    bye()

greet("kirill")
