def menu():
    m = int(input("menu de opciones : "))

    diccionario = {}
    for y in range(1,m+1):

        f = input("Digite la funcion: ")
        df = input("Su Descripcion: ")
        diccionario[y] = (df,f)

    print("\n\n\nBienvenido Al Menu")
    for x in diccionario:
        print(f"{x}. {diccionario[x][0]}")
    opcion = int(input("Digite una opcion: "))
    return (opcion,diccionario)

def main():
        
    op = menu()
    
    for clave in op[1]:
        if(op[0]==clave):
            print("El nombre de esta funcion es : ")
            print(op[1][clave][1])
    
if __name__ == "__main__":
    main()
