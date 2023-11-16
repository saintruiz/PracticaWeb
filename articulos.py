
Artículos_disponibles={
    "Lapicero":2300,
    "Bloc": 4500,
    "Borrador": 1200,
    "Cuaderno": 2800
}
def precio_articulo(articulo, cantidad):
    if articulo in Artículos_disponibles:
        return (Artículos_disponibles[articulo])*cantidad
    else:
        return "El articulo no se encuentra en el sistema"

articulo=input()
cantidad=int(input())
print(precio_articulo(articulo, cantidad))