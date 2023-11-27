class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class ArbolBinario: 
    def __init__(self):
        self.raiz =  None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo, nuevo_dato):
        if nuevo_dato == nodo.dato:
            print(f"El día {nuevo_dato} ya existe en el Árbol.")
            return

        if nuevo_dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = NodoArbol(nuevo_dato)
            else:
                self._insertar_recursivo(nodo.izquierda, nuevo_dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoArbol(nuevo_dato)
            else:
                self._insertar_recursivo(nodo.derecha, nuevo_dato)

    def mostrar_arbol(self):
        self._mostrar_arbol_recursivo(self.raiz, 0)

    def _mostrar_arbol_recursivo(self, nodo, nivel):
        if nodo is not None:
            self._mostrar_arbol_recursivo(nodo.derecha, nivel + 1)
            print("    " * nivel + str(nodo.dato))
            self._mostrar_arbol_recursivo(nodo.izquierda, nivel + 1)

    def buscar(self, dato):
        return self._buscar_recursivo(self.raiz, dato)

    def _buscar_recursivo(self, nodo, dato):
        if nodo is None or nodo.dato == dato:
            return nodo
        if dato < nodo.dato:
            return self._buscar_recursivo(nodo.izquierda, dato)
        return self._buscar_recursivo(nodo.derecha, dato)

    def eliminar(self, dato):
        self.raiz = self._eliminar_recursivo(self.raiz, dato)

    def _eliminar_recursivo(self, nodo, dato):
        if nodo is None:
            return nodo
        if dato < nodo.dato:
            nodo.izquierda = self._eliminar_recursivo(nodo.izquierda, dato)
        elif dato > nodo.dato:
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, dato)
        else:
            if nodo.izquierda is None:
                return nodo.derecha
            elif nodo.derecha is None:
                return nodo.izquierda
            nodo.dato = self._encontrar_minimo(nodo.derecha)
            nodo.derecha = self._eliminar_recursivo(nodo.derecha, nodo.dato)
        return nodo

    def _encontrar_minimo(self, nodo):
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual.dato

    def recorrer_preOrden(self):
        resultado = []
        self.preOrden(self.raiz, resultado)
        return resultado

    def preOrden(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.dato)
            self.preOrden(nodo.izquierda, resultado)
            self.preOrden(nodo.derecha, resultado)

    def recorrer_inOrden(self):
        resultado = []
        self.inOrden(self.raiz, resultado)
        return resultado

    def inOrden(self, nodo, resultado):
        if nodo is not None:
            self.inOrden(nodo.izquierda, resultado)
            resultado.append(nodo.dato)
            self.inOrden(nodo.derecha, resultado)

    def recorrer_postOrden(self):
        resultado = []
        self.postOrden(self.raiz, resultado)
        return resultado

    def postOrden(self, nodo, resultado):
        if nodo is not None:
            self.postOrden(nodo.izquierda, resultado)
            self.postOrden(nodo.derecha, resultado)
            resultado.append(nodo.dato)

arbol = ArbolBinario()
dias_para_insertar = ['Viernes', 'Martes', 'Lunes', 'Domingo', 'Jueves', 'Miércoles', 'Sábado']
for dia in dias_para_insertar:
    arbol.insertar(dia)
arbol.mostrar_arbol()
while True:
    respuesta = input("¿Desea ingresar días al Árbol? (si/no): ").lower()

    if respuesta != 'si':
        break

    dias_ingresar = input("Ingrese los días que desea poner en el Árbol separados por un espacio: ")
    dias_ingresar = [dia.capitalize() for dia in dias_ingresar.split()]

    for dia_ingresar in dias_ingresar:
        arbol.insertar(dia_ingresar)
arbol.mostrar_arbol()

dia_buscar = input("¿Qué día quieres buscar? ").capitalize()
nodo_encontrado = arbol.buscar(dia_buscar)
if nodo_encontrado:
    print(f"El día {dia_buscar} fue encontrado en el Árbol.")
else:
    print(f"El día {dia_buscar} no fue encontrado en el Árbol")

dia_eliminar = input("Ingresa el día que quieres eliminar: ").capitalize()
nodo_encontrado = arbol.buscar(dia_eliminar)

if nodo_encontrado:
    arbol.eliminar(dia_eliminar)
    print(f"Se eliminó el día {dia_eliminar} correctamente del Árbol")
else:
    print(f"El día {dia_eliminar} no existe en el Árbol")
arbol.mostrar_arbol()
print("El recorrido en PreOrden es: ", arbol.recorrer_preOrden())
print("El recorrido en InOrden es: ", arbol.recorrer_inOrden())
print("El recorrido en PostOrden es: ", arbol.recorrer_postOrden())
