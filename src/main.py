from kb import FACTS, COORDS
from search import RouteFinder

if __name__ == '__main__':
    rf = RouteFinder(FACTS, coords=COORDS, transfer_penalty=4)
    res = rf.a_star('A', 'C')

    if res is None:
        print("No se encontró ruta entre A y C")
    else:
        print('Mejor ruta encontrada:')
        for node, line in res['path']:
            print(f"{node} (línea: {line})")
        print('Costo total (minutos):', res['cost_minutes'])
