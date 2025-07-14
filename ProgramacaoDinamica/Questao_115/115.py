from typing import List
class Solution:
    def numDistinct(self, origem: str, destino: str) -> int:
        n, m = len(origem), len(destino)  # Tamanhos das strings
        tabela = self.criar_tabela(n, m)  # Cria matriz vazia
        self.inicializar_primeira_coluna(tabela, n)  # Inicializa coluna 0
        self.atualizar_tabela(tabela, origem, destino, n, m)  
        return tabela[n][m]  
    def criar_tabela(self, linhas: int, colunas: int) -> List[List[int]]:
        return [[0] * (colunas + 1) for _ in range(linhas + 1)]  # Cria matriz zerada
    def inicializar_primeira_coluna(self, tabela: List[List[int]], linhas: int) -> None:
        indice = 0  
        while indice <= linhas:
            tabela[indice][0] = 1  
            indice += 1  # Avança índice
    def atualizar_tabela(self, tabela: List[List[int]], origem: str, destino: str, linhas: int, colunas: int) -> None:
        linha = 1  # Linha inicial
        while linha <= linhas:  # Percorre origem
            coluna = 1  # Coluna inicial
            while coluna <= colunas:  # Percorre destino
                if origem[linha - 1] == destino[coluna - 1]:  # Se iguais
                    tabela[linha][coluna] = tabela[linha - 1][coluna - 1] + tabela[linha - 1][coluna]  # Soma caminhos
                else:
                    tabela[linha][coluna] = tabela[linha - 1][coluna]  # Pula caractere da origem
                coluna += 1  # Avança coluna
            linha += 1  # Avança linha
