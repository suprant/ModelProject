def Outer_Function():
    print("Hei Outer Function")
    def Inner_Function():
        print("Hello Inner Function")
    Inner_Function()
Outer_Function()