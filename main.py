from funciones import *


def solucion(f: int, c: int, laberinto: list[list[str]], matrizVis: list[list[int]], contador: int, mejor_solucion: SolucionOptima, salida: tuple, portales: dict):
    distancia_restante = calcular_distancia((f, c), salida)
    portales = buscarPortales(laberinto)
    posiblePortal = distanciaPortal((f, c), portales, salida)
    if (contador - posiblePortal >= mejor_solucion.mejor_camino or distancia_restante + contador > mejor_solucion.mejor_camino) and mejor_solucion.mejor_camino != -1:
        print("PODA!")
        return
    if laberinto[f][c] == "S":
        if contador < mejor_solucion.mejor_camino or mejor_solucion.mejor_camino == -1:
            mejor_solucion.mejor_camino = contador
        return

    matrizVis[f][c] = 1

    if laberinto[f][c] not in ["#", ".", "E", "S"]:
        otroPortal = buscarPortal(laberinto, (f, c), laberinto[f][c])
        if len(otroPortal) == 2 and matrizVis[otroPortal[0]][otroPortal[1]] != 1:
            temporalcar = laberinto[f][c]
            laberinto[f][c] = "."
            laberinto[otroPortal[0]][otroPortal[1]] = "."
            solucion(otroPortal[0], otroPortal[1], laberinto,
                     matrizVis, contador + 1, mejor_solucion, salida, portales)
            laberinto[f][c] = temporalcar
            laberinto[otroPortal[0]][otroPortal[1]] = temporalcar

    for i in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if esPosible(f + i[0], c + i[1], laberinto) and matrizVis[f + i[0]][c + i[1]] != 1:
            solucion(f + i[0], c + i[1], laberinto, matrizVis,
                     contador + 1, mejor_solucion, salida, portales)
    matrizVis[f][c] = 0


def main():
    laberinto = abrirLaberinto("laberinto.txt")
    entrada = encontrarCaracter(laberinto, 'E')
    salida = encontrarCaracter(laberinto, 'S')
    matrizVisitados = [
        [0 for _ in range(len(laberinto[0]))] for _ in range(len(laberinto))]
    mejor_solucion = SolucionOptima()
    solucion(entrada[0], entrada[1], laberinto,
             matrizVisitados, 0, mejor_solucion, salida, buscarPortales(laberinto))
    print("Mejor solución:", mejor_solucion.mejor_camino)


if __name__ == "__main__":
    main()
