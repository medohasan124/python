#الهدف هنا اني اشاور علي مكان الداله واضعها في متغير 
def make_greeting(greeting_word):
    def greet(name):
        return f"{greeting_word}, {name}!"
    return greet

english_greeting = make_greeting("Hello")
arabic_greeting = make_greeting("Ahlan")

print(english_greeting("Mohamed"))
print(arabic_greeting("Mohamed"))