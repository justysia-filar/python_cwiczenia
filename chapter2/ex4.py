print("KALKULATOR KOSZTOW SPROWADZENIA SAMOCHODU")

cenaPoczatkowa = float(input("Podaj cene poczatkowa samochodu: " ) )
podatek20 = float(cenaPoczatkowa * 0.20 )
oplata17 = cenaPoczatkowa * 0.17
prowizja = 200
dostarczenie = 678
calkowita = cenaPoczatkowa + podatek20 + oplata17 + dostarczenie + prowizja 

print("podatek 20%:")
print(podatek20)

print("oplata rejestracyjna 17%:")
print(oplata17)

print("oplaty dodatkowe:\nprowizja dilera:")
print(prowizja)

print("dostarczenie do kienta:")
print(dostarczenie)

print("CALKOWITA CENA SAMOCHODU:")
print(calkowita)
