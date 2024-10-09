from lib import cuadrado, triangulo, rectangulo, circunferencia
print("Proyecto Figuras")
print(cuadrado.get_identificador())
lado=4
print(f"El area de un cuadrado de lado {lado} es: {cuadrado.get_area(lado)} y el perímetro es: {cuadrado.get_perimetro(lado)}")

base=4
altura=2
print(triangulo.get_identificador())
print(f"El area de un triángulo de base {base} y de altura {altura} es: {triangulo.get_area(base, altura)} y el perímetro es: {triangulo.get_perimetro(base, base, base)}")
print(rectangulo.get_identificador())
print(f"El area de un rectángulo de base {base}\
     y altura {altura} es: {rectangulo.get_area(base, altura)} \
     y el perímetro es: {rectangulo.get_perimetro(base, altura)}")

radio = 4
print(f"El area de una circunferencia de radio {radio} es: {circunferencia.get_area(radio)}")