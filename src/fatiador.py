# este arquivo trata os processos de fatiar uma imagem, com base em uma grid
import numpy as np
import math

class Fatiador:

    # construtor da classe
    def __init__(self, dimensoes: tuple, quadranteMinimo: int = 128):
        self.largura = dimensoes[0]
        self.altura = dimensoes[1]
        self.quadranteMinimo = quadranteMinimo
        self.quadranteMinimoAltura = 0
        self.quadranteMinimoLargura = 0
    

    # validar o quadrante minumo
    def __padronizarQuadranteMinimo(self):
        # o quadrante não pode ser maior do que a largura ou altura da imagem
        if( self.quadranteMinimo < self.largura | self.quadranteMinimo < self.altura ):
            self.quadranteMinimo = ( self.altura, self.largura )[self.largura < self.altura] # teste if ternario (falseValue, trueValue)[test]
        
        # o quadrante mínimo não pode ser menor do que 2 pixels
        if( self.quadranteMinimo < 2 ):
            raise Exception("O valor do quadrante mínimo deve ser maior ou igual a 2")
        
        # a largura não pode ser menor do que 2 pixels
        if( self.largura < 2 ):
            raise Exception("A largura mínima deve ser maior ou igual a 2")
        
        # a altura mínima não pode ser menor do que 2 pixels
        if( self.altura < 2 ):
            raise Exception("A altura mínima deve ser maior ou igual a 2")

        


    # executa o calculo de divisão das fatias, com base no quadrante minimo
