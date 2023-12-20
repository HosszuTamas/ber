from dolgozok import Dolgozo
class Ber:
    def __init__(self):
        self.filename="berkft.txt"
        self.dolgozoLista=[]

    def olvas_fajl(self):
        fp=open(self.filename, "r", encoding="utf-8")
        lines=fp.readlines()
        fp.close()
        for line in lines:
            line=line.rstrip()
            (nev, telepules, cim, szuletes, fizetes)=line.split(":")
            dolgozo=Dolgozo(nev, telepules, cim, szuletes, fizetes)
            self.dolgozoLista.append(dolgozo)
# print(dolgozo.fizetes)
            
    def szolnoki(self):
        szolnokiLista=[]
        for dolgozo in self.dolgozoLista:
            if dolgozo.telepules=="Szolnok":
                szolnokiLista.append(dolgozo)
                
        max_szolnoki=szolnokiLista[0]
        for szolnoki in szolnokiLista:
            if szolnoki.szuletes>max_szolnoki.szuletes:
                max_szolnoki=szolnoki
        print(max_szolnoki.szuletes)
ber=Ber()
ber.olvas_fajl()
ber.szolnoki()