def escreva(txt):
    print("~" * (len(txt) + 4))
    print(f"  {txt}")
    print("~" * (len(txt) + 4))
msg = str(input("Titulo: "))
escreva(msg)
