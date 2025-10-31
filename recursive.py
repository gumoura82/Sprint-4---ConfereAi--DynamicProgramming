# Arquivo: recursive.py
from functools import lru_cache
from typing import List, Tuple, Optional

def wagner_whitin_topdown(demanda: List[int], K: float, h: float, validade: Optional[int]=None):
    """
    Calcula o custo ótimo usando a abordagem Top-Down (Recursiva com Memoization).
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

    @lru_cache(None)
    def F(t):
        if t > n:
            return 0.0
        
        best = float('inf')
        max_j = n if validade is None else min(n, t + validade - 1)
        
        for j in range(t, max_j + 1):
            cost = K + holding_cost(t, j) + F(j+1)
            if cost < best:
                best = cost
        return best

    # --- Reconstrução da Política ---
    politica = []
    t = 1
    while t <= n:
        best = float('inf')
        argj = None
        max_j = n if validade is None else min(n, t + validade - 1)
        
        for j in range(t, max_j + 1):
            cost = K + holding_cost(t, j) + F(j+1) 
            if cost < best:
                best = cost
                argj = j
                
        if argj is not None:
            qtd = soma(t, argj)
            politica.append((t, argj, qtd))
            t = argj + 1
        else:
            t = n + 1 

    return F(1), politica