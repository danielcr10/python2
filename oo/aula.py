import ponto

if __name__ == "__main__":
    p1 = ponto.Ponto()
    p2 = ponto.Ponto(3,1)
    p3 = ponto.Ponto(1,3)

    a = p1.distancia(p2)
    b = p2.distancia(p3)
    c = p1.distancia(p3)
    abs(a-b)
    