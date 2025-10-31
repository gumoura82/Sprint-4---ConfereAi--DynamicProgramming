# Arquivo: example.py
from recursive import wagner_whitin_topdown
from bottomup import wagner_whitin_bottomup

# --- Exemplo de como usar ---
if __name__ == '__main__':
    # Exemplo clássico
    demanda_exemplo = [10, 20, 5, 25, 10]
    K_exemplo = 100  # Custo fixo do pedido
    h_exemplo = 1    # Custo de manutenção por unidade por período

    # Testando a versão Top-Down (Recursiva)
    custo_td, politica_td = wagner_whitin_topdown(demanda_exemplo, K_exemplo, h_exemplo)
    print(f"--- Top-Down (Recursivo) ---")
    print(f"Custo Total Mínimo: {custo_td}")
    print(f"Política de Pedidos: {politica_td}")
    # Política: (Período do Pedido, Atende até Período, Quantidade)

    print("\n" + "="*30 + "\n")

    # Testando a versão Bottom-Up (Iterativa)
    custo_bu, politica_bu = wagner_whitin_bottomup(demanda_exemplo, K_exemplo, h_exemplo)
    print(f"--- Bottom-Up (Iterativo) ---")
    print(f"Custo Total Mínimo: {custo_bu}")
    print(f"Política de Pedidos: {politica_bu}")