'''
Created on 20200710
Update on 20200710
@author: Eduardo Pagotto
 '''

from typing import List, Tuple, Any

valX: str = 'Xena'

#def soma(val_a, val_b) -> int:
def soma(val_a: int, val_b: int) -> int:
    """[Soma de Valores]
    Args:
        val_a (int): [Primeiro valor]
        val_b (int): [Segundo valor]
    Returns:
        int: [reusltado soma]
    """

    resultado: int = val_a + val_b

    return resultado


if __name__ == "__main__":

    pontos: List[Tuple[int, int]] = [(1, 2), (3, 4), (5, 6)]

    val_resultado: int = soma(1, 3)
    print(val_resultado)

    val_teste: int = soma(1, 3)
    print(val_teste)

    r: int = soma(5, 7) + 5 #'banana'
    print(r)

    #print(soma.__doc__)
    #print(soma.__annotations__)
    # print(__annotations__)
