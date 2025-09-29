# search.py
import heapq
from math import sqrt

class RouteFinder:
    def __init__(self, facts, coords=None, transfer_penalty=4):
        """
        facts: lista de tuplas (origen, destino, línea, tiempo, distancia)
        coords: diccionario {nodo: (x, y)} para heurística euclidiana
        transfer_penalty: penalización (en minutos) por cambiar de línea
        """
        self.graph = {}  # node -> list of (neighbor, line, travel_time, distance)
        self.coords = coords or {}
        self.transfer_penalty = transfer_penalty

        # construir grafo no dirigido
        for a, b, line, t, d in facts:
            self.graph.setdefault(a, []).append((b, line, t, d))
            self.graph.setdefault(b, []).append((a, line, t, d))

    def heuristic(self, n1, n2):
        """Distancia heurística entre nodos (euclidiana si hay coords, si no, 0)."""
        if n1 in self.coords and n2 in self.coords:
            x1, y1 = self.coords[n1]
            x2, y2 = self.coords[n2]
            return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) * 2.0  # factor para aproximar minutos
        return 0

    def neighbors(self, node):
        return self.graph.get(node, [])

    def a_star(self, start, goal, prefer_few_transfers=False, debug=False):
        """
        Busca la mejor ruta entre start y goal usando A*.
        Devuelve un diccionario con 'path' y 'cost_minutes' o None si no hay ruta.
        """
        start_state = (start, None)  # (nodo actual, línea actual)
        open_heap = []
        heapq.heappush(open_heap, (0 + self.heuristic(start, goal), 0, start_state, []))
        visited = set()

        while open_heap:
            f, g, (node, cur_line), path = heapq.heappop(open_heap)

            if debug:
                print(f"Visitando {node}, costo acumulado={g}, línea={cur_line}")

            if node == goal:
                return {
                    "path": path + [(node, cur_line)],
                    "cost_minutes": g
                }

            if (node, cur_line) in visited:
                continue
            visited.add((node, cur_line))

            for (nbr, line, ttime, _) in self.neighbors(node):
                extra = 0
                if cur_line is not None and cur_line != line:
                    # penalización por transferencia
                    extra += self.transfer_penalty
                new_g = g + ttime + extra
                h = self.heuristic(nbr, goal)
                new_state = (nbr, line)

                # si se prefiere menos transbordos, añadimos una pequeña penalización adicional
                if prefer_few_transfers and cur_line is not None and cur_line != line:
                    new_g += 1.5

                heapq.heappush(
                    open_heap,
                    (new_g + h, new_g, new_state, path + [(node, cur_line)])
                )

        return None