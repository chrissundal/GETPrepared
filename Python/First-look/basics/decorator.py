def cough_dec(func):
    def func_wrapper():
        # kode før funksjon
        print("*kremter*")
        func() # funksjon
        # kode etter funksjon
        print("*kremter*")
    return func_wrapper

@cough_dec
def question():
    print("kan du gi meg noe rabatt?")

@cough_dec
def answer():
    import random
    randomnumber = random.randint(1, 15)
    print(f"ja, du får {randomnumber}% rabatt")