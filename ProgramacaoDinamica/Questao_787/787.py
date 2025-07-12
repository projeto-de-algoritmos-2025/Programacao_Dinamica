from typing import List
class Solution:
    def findCheapestPrice(self, total_cidades: int, voos: List[List[int]], origem: int, destino: int, max_paradas: int) -> int:
        INFINITO = float('inf')  # Valor infinito para inicialização
        tabela_distancias = self.iniciar_tabela(total_cidades, origem, INFINITO)  # Cria vetor inicial de distâncias
        repeticao = 0  
        rotas = self.montar_rotas(total_cidades, voos)   
        while repeticao <= max_paradas:  # Executa até o limite de paradas
            tabela_distancias = self.processar_rotas(rotas, tabela_distancias, INFINITO)  
            repeticao += 1  # Incrementa repetição
        return -1 if tabela_distancias[destino] == INFINITO else tabela_distancias[destino]  # Retorna resultado
    def iniciar_tabela(self, quantidade: int, ponto_inicial: int, infinito: float) -> List[float]:
        tabela = [infinito] * quantidade  # Cria lista com infinito
        tabela[ponto_inicial] = 0  
        return tabela  
    def montar_rotas(self, quantidade: int, lista_voos: List[List[int]]) -> List[List[tuple]]:
        indice_rota = 0  
        rotas = [[] for _ in range(quantidade)]  # Inicializa lista de listas
        while indice_rota < len(lista_voos):  # Percorre todos os voos
            partida, chegada, custo_trecho = lista_voos[indice_rota]  # Desempacota voo
            rotas[partida].append((chegada, custo_trecho))  # Adiciona vizinho
            indice_rota += 1  # Avança índice
        return rotas  # Retorna rotas
    def processar_rotas(self, rotas: List[List[tuple]], tabela_atual: List[float], infinito: float) -> List[float]:
        indice_partida = 0  
        nova_tabela = tabela_atual.copy()  # Copia tabela para atualizar
        while indice_partida < len(rotas):  # Percorre todas as cidades
            if tabela_atual[indice_partida] != infinito:  
                indice_trecho = 0  
                vizinhos = rotas[indice_partida]  
                while indice_trecho < len(vizinhos):  # Percorre vizinhos
                    chegada, custo = vizinhos[indice_trecho]  # Desempacota destino e custo
                    if tabela_atual[indice_partida] + custo < nova_tabela[chegada]:  
                        nova_tabela[chegada] = tabela_atual[indice_partida] + custo  # Atualiza custo
                    indice_trecho += 1  # Próximo vizinho
            indice_partida += 1  # Próxima cidade
        return nova_tabela  # Retorna tabela 
