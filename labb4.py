import random

def start():
  saldo = 100
  return saldo
saldo = start()

def kasta_tarning():
  x = random.randint(1,6)
  return x

def spelarens_kast(x):
  print("saldo=", x)
  bet = 0
  bet = int(input("hur mycket vill du beta:"))
  while x <= bet or 0 < bet:
    bet = int(input("beta något du har råd med:"))
  spelarens_resultat = kasta_tarning()
  print(spelarens_resultat)
  y = input("kasta igen?")
  while y == "ja":
    spelarens_resultat += kasta_tarning() + kasta_tarning()
    print(spelarens_resultat)
    if spelarens_resultat > 21:
      print("du bliv tjock")
      spelarens_resultat=-1
      return spelarens_resultat, bet
    y = input("kasta igen?")
    if y == "nej":
      return spelarens_resultat, bet
  return spelarens_resultat, bet
    

def dealerns_kast():
  dealerns_resultat = kasta_tarning()
  while dealerns_resultat < 17:
    dealerns_resultat += kasta_tarning()
    if dealerns_resultat > 21:
      print("dealern bliv tjock")
      dealerns_resultat=0
      return dealerns_resultat
  print(dealerns_resultat) 
  return dealerns_resultat

def avgora_vinnaren(x):
  spelare_poang, bet = spelarens_kast(x)
  dealer_poang = dealerns_kast()
  if spelare_poang > dealer_poang:
    print("du van")
    saldo = x + bet*2
  elif spelare_poang == dealer_poang:
    print("oavgjort")
  else:
    print("du förlorade")
    saldo = x - bet
    return saldo

def spela_igen():
  x = input("vill du köra om?")
  if x == "nej":
    print("hejdå")
    exit()
  elif x == "ja":
    print("lucka till")
    
def main(saldo):

  while True:
    saldo = avgora_vinnaren(saldo)
    spela_igen()
   
main(saldo)