"""fonction racine carrée de math"""
from math import sqrt

#### Fonction secondaire

def isprime(p: int) -> bool:
    """fonction premettant de retourner si le param p est premier ou non.
    Args:
        p (int): nombre à tester.
    Returns:
        bool: True si premier, False sinon.
    """
    if p<2:
        return False
    for i in range(2,round(sqrt(p)+1)):
        if p % i == 0:
            return False
    return True
#### Fonction principale

def main():
    """
    La fonction main
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
