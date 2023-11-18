def name_checker(counter):
    while True:
        name = str(input(f"\n\n\nAdd meg a {counter}. tantárgy nevét: "))
        if not name.isalpha():
            print("A tantárgy neve csak betűket tartalmazhat, szóközt sem!")
        elif not name[0].isupper():
            print("A tantárgy neve csak nagy betűvel kezdődhet!")
        elif len(name) < 4:
            print("A tantárgy neve nem lehet 4 betűsnél rövidebb!")
        else:
            return name
    
def percent_checker():
    while True:
        percent = input("\nKérlek, add meg az elért százalékot: ")
        if not percent.isdigit():
            print("A százalék csak egész szám lehet!")
        else:
            percent = int(percent)
            if not ((percent >= 0) and (percent <= 100)):
                print("A százalék csak 0 és 100 közötti egész szám lehet!")
            else:
                return percent
    
def grade_checker():
    while True:
        grade = input("\nKérlek, add meg a 11. évvégi érdemjegyed: ")
        if not grade.isdigit():
            print("Az érdemjegy csak egész szám lehet!")
        else:
            grade = int(grade)
            if not ((grade >= 1) and (grade <= 5)):
                print("Az érdemjegy csak 1 és 5 közötti egész szám lehet!")
            else:
                return grade
    
def grade2_checker():
    while True:
        grade2 = input("\nKérlek, add meg a 12. évvégi érdemjegyed: ")
        if not grade2.isdigit():
            print("Az érdemjegy csak egész szám lehet!")
        else:
            grade2 = int(grade2)
            if not ((grade2 >= 1) and (grade2 <= 5)):
                print("Az érdemjegy csak 1 és 5 közötti egész szám lehet!")
            else:
                return grade2
                
def advanced_checker():
    while True:
        advanced = str(input("\nEmelt szintű? (Igen/Nem): "))
        if not advanced.isalpha():
            print("A logikai érték csak betűket tartalmazhat, szóközt sem!")
        elif advanced.lower() in ("igen", "i"):
            return True
        elif advanced.lower() in ("nem", "n"):
            return False
        else:
            print("A logikai érték nem megfelő vagy nem helyen lett beírva!")
    
def priority_checker():
    while True:
        priority = str(input("\nKiemelten számít a felvételi eljárásban? (Igen/Nem): "))
        if not priority.isalpha():
            print("A logikai érték csak betűket tartalmazhat, szóközt sem!")
        elif priority.lower() in ("igen", "i"):
            return True
        elif priority.lower() in ("nem", "n"):
            return False
        else:
            print("A logikai érték nem megfelő vagy nem helyen lett beírva!")

def quantity_input(): # Tantárgyak darabszáma függvény
    while True:
            quantity = input("\nKérlek, add meg, hogy hány tantárgyból érettségiztél: ")
            if not quantity.isdigit():
                print("A tantárgyak száma csak egész szám lehet!")
            else:
                quantity = int(quantity)
                if not ((quantity >= 5) and (quantity <= 15)):
                    print("A tantárgyak száma csak 5 és 15 közötti egész szám lehet!")
                else:
                    return quantity

class Subject: # Tantárgyak tulajdonságai
    def __init__(self, id, name, percent, grade, grade2, advanced=False, priority=False):
        self.id = id
        self.name = name
        self.percent = percent
        self.grade = grade
        self.grade2 = grade2
        self.advanced = advanced
        self.priority = priority

def total_points(subjects, extra): # Összpontszám számító
    percent_points = [] # érettségi pontok
    percents = [] # minden százalék
    grade_points = [] # minden tantárgy jegyeiért 2 pont. 5-ös 10 pont. 2x5-ös az 20 pont
    for subject in subjects:
        if subject.priority:
            if subject.advanced:
                percent_points.append(subject.percent)
            else:
                percent_points.append(int(round((subject.percent*0.67),0)))
                
        percents.append(subject.percent)
        
        grade_points.append((subject.grade + subject.grade2)*2)


    percent_point = sum(percent_points) # érettségi pontok
    if percent_point > 200:
        percent_point = 200
    
    percent_avg = int(round(sum(percents)/len(percents),0))
    grade_point = sum(grade_points) + percent_avg # tanulmányi pontok
    if grade_point > 200:
        grade_point = 200

    points = int(percent_point + grade_point + extra) # végleges összpontszám
    return points

def display_table(subjects, extra): # Táblázat
    print("\n\n\n")
    
    header = f"{'ID':<5}{'Tantárgy neve':<20}{'Elért százalék':<15}{'11. évvégi érdemjegy':<25}{'12. évvégi érdemjegy':<25}{'Emelt szintű':<15}{'Kiemelten számít a felvételi eljárásban':<40}"
    print(header)
    print("=" * len(header)) # fejléc

    for subject in subjects:
        advanced_str = "Igen" if subject.advanced else "Nem"
        priority_str = "Igen" if subject.priority else "Nem"

        print(f"{subject.id:<5}{subject.name:<20}{subject.percent:<15}{subject.grade:<25}{subject.grade2:<25}{advanced_str:<15}{priority_str:<40}")
    
    print(f"\nA pluszpontjaid száma: {extra} pont.")
    print(f"\nAz összesített pontszámod: {total_points(subjects, extra)}") # Pontszámok megjelenítése
    
    selection(subjects,extra)

def extra_input():
    while True:
            extra = input("\nKérlek, add meg a pluszpontjaid számát: ") # Pluszpontok input
            if not extra.isdigit():
                print("Az pluszpontok száma csak egész szám lehet!")
            else:
                extra = int(extra)
                if not ((extra >= 0) and (extra <= 100)):
                    print("Az pluszpontok száma csak 1 és 100 közötti egész szám lehet!")
                else:
                    return extra

def editor(subjects, extra): # Adatmódosítás
    while True:
        which1 = str(input("\n\n\nKérlek, add meg, min szeretnél módosítani (Pluszpont/Tantárgy azonosítója): ")).lower()
        ids = []
        for subject in subjects:
            ids.append(str(subject.id))
            
        if which1 in ("kilépés", "kilép", "kilepes", "kilep"):
            exit()
        elif which1 in ("pluszpontok", "pluszpont", "plusz", "pp" "p", "extra", "e"):
            extra = extra_input()
            display_table(subjects,extra)
        elif which1 in ids:
            which_subject = ""
            for subject in subjects:
                if which1 == str(subject.id):
                    which_subject = subject.name
                    print(f"\nTe a {subject.name} tantárgy adatait szeretnéd módosítani.")
                    while True:
                        which2 = str(input(f"\nKérlek, add meg annak az azonosítóját, amelyiket módosítani szeretnéd:\n1.: Tantárgy neve - {subject.name}\n2.: Elért százalék - {subject.percent} %\n3.: 11. évvégi érdemjegy - {subject.grade}\n4.: 12. évvégi érdemjegy - {subject.grade2}\n5.: Emelt - {'Igen' if subject.advanced else 'Nem'}\n6.: Kiemelt - {'Igen' if subject.advanced else 'Nem'}\n>>> "))
                        if not which2.isdigit():
                            print("Nem adhatsz meg mást, csak számokat.")
                        elif which2 == "1":
                            subject.name = name_checker(counter=1)
                            display_table(subjects,extra)
                        elif which2 == "2":
                            subject.percent = percent_checker()
                            display_table(subjects,extra)
                        elif which2 == "3":
                            subject.grade = grade_checker()
                            display_table(subjects,extra)
                        elif which2 == "4":
                            subject.grade2 = grade2_checker()
                            display_table(subjects,extra)
                        elif which2 == "5":
                            subject.advanced = advanced_checker()
                            display_table(subjects,extra)
                        elif which2 == "6":
                            subject.priority = priority_checker()
                            display_table(subjects,extra)
                        else:
                            print("Valamit rosszul adtál meg.")
                        

def selection(subjects, extra): # Input után mit akar a user
    while True:
        ask = str(input("\nKérlek, add meg, hogy mit szeretnél tenni (Kilépés/Adatmódosítás): ")).lower()
        if not ask.isalpha():
            print("Nem tartalmazhat mást, csak betűket, szóközt sem!")
        elif ask in ("kilépés", "kilép", "kilepes", "kilep", "ki", "k"):
            exit()
        elif ask in ("adatmódosítás", "módosítás", "adatmodositas", "modositas", "módosít", "modosit", "adm", "am", "m"):
            editor(subjects, extra)
            break
        else:
            print("Nem jó szót adtál meg!")        

def handler(): # Programkezelő függvény
    quantity = quantity_input()
    subjects = []
    counter = 1
    for i in range(quantity):
        subject_data = name_checker(counter), percent_checker(), grade_checker(), grade2_checker(), advanced_checker(), priority_checker()
        subject = Subject(i + 1, *subject_data)
        subjects.append(subject)
        counter += 1
    
    extra = extra_input()
    
    display_table(subjects,extra)
    
    return
handler()