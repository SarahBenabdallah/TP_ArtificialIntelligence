class Fait :
    def __init__(self,fait,explication):
        self.fait = fait
        self.explication = explication

    def print_fait(self):
        print("Fait :",self.fait)
        print("Explication: ",self.explication )

class Regle:
    def __init__(self,regle,premisse,conclusion):
        self.regle = regle
        self.premisse = premisse
        self.conclusion = conclusion
    def print_regle(self):
        print("reg:",self.regle)
        print("prem: ",self.premisse )
        print("conc :", self.conclusion)

def lire_fait():
    file = input("selection la base des faits: ")
    f= open(file,"r")
    line =f.readline().strip()
    base_fait = list()
    while line: 
        base_fait.append(
            Fait(line,-1)
        )
        line = f.readline().strip()
        #print(line)
    f.close()
    return base_fait

def lire_regle():
    file = input("selection la base des regles: ")
    f= open(file,"r")
    line =f.readline()
    base_regle = list()
    while line : 
        aux = line.split(":")
        regle = aux[0].strip()
        premisse = aux[1][ 
            aux[1].find("si") +2 : 
            aux[1].find("alors")
        ].strip().split(' et ')
        conclusion = aux[1].split('alors')[1].strip().split("et")
        base_regle.append(
            Regle(
                regle,
                premisse,
                conclusion
            )
        )
        line =f.readline()
    f.close()
    return base_regle

def in_base(base_fait,fait):
    for i in range(0,len(base_fait)):
        if fait == base_fait[i].fait :
            return True
    return False

def test(prem,tab):
    for j in range(0,len(prem)):
        if not(prem[j] in tab):
            return False
    return True

def chainage_avant(base_fait,base_regle,fait) : 
    tab_fait = list()
    #creation d'un tableau de fait
    for i in range(0,len(base_fait)):
        tab_fait.append(base_fait[i].fait)

    while not(in_base(base_fait,fait)):
        nb_fait = len(tab_fait)
        for i in range(0,len(base_regle)):

            prem =base_regle[i].premisse
            if test(prem,tab_fait):
                for k in range(0,len(base_regle[i].conclusion)):
                    base_fait.append(
                        Fait(
                            base_regle[i].conclusion[k],
                            base_regle[i].regle
                        )
                    )
                    tab_fait.append(base_regle[i].conclusion[k].strip())

                base_regle.remove(base_regle[i])
                #print(tab_fait)
                break
        if nb_fait == len(tab_fait):
            break 
    if fait in tab_fait:
        print(fait+ " établi")
    else :
        print(fait + " non-établi")

def print_base_f(base):
    for index in range (0, len(base)):
        base[index].print_fait()
        print("----------------------")
def print_base_r(base):
    for index in range (0, len(base)):
        base[index].print_regle()
        print("----------------------")

if __name__=="__main__":
    base_fait = list()
    base_regle= list()
    but = str()
    while True:
        print(
            "q: quit\nf: changer bf\nr: changer br\nb: but\np: parametre\ne: executer"
        )
        text = input("> ")
        if text == "q":
            break
        elif text == "f":
                base_fait = lire_fait()  
                print_base_f(base_fait)
        elif text =="r":
            base_regle = lire_regle()
            print_base_r(base_regle)
        elif text == "b":
            but =input("Saisir vote but: ")
        elif text =="p":
            print("Base des faits:")
            print_base_f(base_fait)
            print("Base des regles:")
            print_base_r(base_regle)
            print("But: ",but)
        elif text=="e":
                chainage_avant(base_fait,base_regle,but)


