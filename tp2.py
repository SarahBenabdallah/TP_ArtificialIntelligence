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
    file = input("Veuillez sélectionner la base des faits: ")
    f= open(file,"r")
    line =f.readline().strip()
    base_fait = list()
    while line: 
        base_fait.append(
            Fait(line,-1) 
        )
        line = f.readline().strip()
        
    f.close()
    return base_fait

def lire_regle():
    file = input("Veuillez sélectionner la base des regles: ")
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

def print_base_f(base):
    for index in range (0, len(base)):
        base[index].print_fait()
        print("----------------------")

def print_base_r(base):
    for index in range (0, len(base)):
        base[index].print_regle()
        print("----------------------")

def chainage_arriere(base_fait,base_regle,but,trace=list()):
    tr = list()
    for b in but :
        if b in base_fait:
            tr.append('-1')
            continue
        for regle in base_regle:
            tr.append(regle.regle)
            if b in regle.conclusion:
                if test(regle.premisse,base_fait):
                    base_fait.append(b)
                    #print(b)
                    break
                else:
                    trace = chainage_arriere(base_fait,base_regle,regle.premisse,tr)
                    if not(trace == list()):
                        base_fait.append(b)
                        tr.append(trace)
                    else:
                        tr.remove(regle.regle)
                        
            else :
                tr.remove(regle.regle)
                #break
    return tr

if __name__=="__main__":
    base_fait = list()
    base_regle= list()
    trace = list()
    but = str()
    while True:
        print(
            "f: Changer base des faits\nr: Changer base des regles\nb: Saisir but\np: Afficher les parametres\nt: Afficher la trace\ns: Sauvgarder la trace\ne: Executer\nq: Quitter\n"
        )
        text = input("> ")
        if text == "q":
            break
        elif text == "f":
                base_fait = lire_fait()  
                #print_base_f(base_fait)
        elif text =="r":
            base_regle = lire_regle()
            #print_base_r(base_regle)
        elif text == "b":
            but =input("Saisir vote but: ")
        
        # elif text=="chainage avant: ":
            # trace = chainage_avant(base_fait,base_regle,but)
             
        elif text =="p":
            print("Base des faits:")
            print_base_f(base_fait)
            print("Base des regles:")
            print_base_r(base_regle)
            print("But: ",but)
        
        elif text =="t":
            print(trace)

        elif text == "s":
            print(trace)
            f = open("trace.txt","w")
            tr=str(trace)
            f.write(tr)
        elif text =="e":
            tab_fait = list()
            #creation d'un tableau de fait
            for ft in base_fait :
                tab_fait.append(ft.fait)
            
            trace = list()
            b = list()
            b.append(but)
            #print(b)
            tr = chainage_arriere(tab_fait,base_regle,b,trace)
            if len(tr) != 0 :
                 print("But atteint")
                 trace = tr
            else:
                print("But non atteint")