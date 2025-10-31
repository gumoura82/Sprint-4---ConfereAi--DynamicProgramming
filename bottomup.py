# Arquivo: bottomup.py
from typing import List, Tuple, Optional

def wagner_whitin_bottomup(demanda: List[int], K: float, h: float, validade: Optional[int]=None):
    """
    Calcula o custo ótimo usando a abordagem Bottom-Up (Iterativa/Tabular).
    """
    n = len(demanda)
    pref = [0]
    for x in demanda:
        pref.append(pref[-1] + x)

    def soma(i, j):
        if i > j: return 0
        return pref[j] - pref[i-1]

    def holding_cost(t, j):
        total = 0
        for r in range(t+1, j+1):
            total += (r - t) * demanda[r-1]
        return h * total

    F = [0.0]*(n+2)
    next_j = [None]*(n+2) 

    for t in range(n, 0, -1):
        best = float('inf')
        argj = None
        max_j = n if validade is None else min(n, t + validade - 1)
        
        for j in range(t, max_j+1):
            cost = K + holding_cost(t, j) + F[j+1]
            if cost < best:
                best = cost
                argj = j
        
        F[t] = best
        next_j[t] = argj 

    # --- Reconstrução da Política ---
    politica = []
    t = 1
    while t <= n:
        j = next_j[t]
        if j is None:
            break
            
        qtd = soma(t, j)
        politica.append((t, j, qtd))
        t = j + 1

    return F[1], politica