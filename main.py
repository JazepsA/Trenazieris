import sqlite3

# Izveido savienojumu ar SQLite datubāzi (tiks izveidota, ja tā neeksistē)
conn = sqlite3.connect('trenazieru_zale.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Sportisti (
    id_sportista INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    dzimšanas_gads INTEGER NOT NULL,
    talrunis TEXT,
    pilsēta TEXT
)
''')

# Tabula "Treneri"
cursor.execute('''
CREATE TABLE IF NOT EXISTS Treneri (
    id_trenera INTEGER PRIMARY KEY AUTOINCREMENT,
    vards TEXT NOT NULL,
    uzvards TEXT NOT NULL,
    izglītība TEXT,
    kvalifikācija TEXT
)
''')

# Tabula "Apmeklējumi"
cursor.execute('''
CREATE TABLE IF NOT EXISTS Apmekleejumi (
    id_apmekleejuma INTEGER PRIMARY KEY AUTOINCREMENT,
    id_sportista INTEGER,
    id_trenera INTEGER,
    datums TEXT NOT NULL,
    nodarbiibas_saakums TEXT,
    nodarbiibas_beigas TEXT,
    laiks INTEGER,
    FOREIGN KEY (id_sportista) REFERENCES Sportisti(id_sportista),
    FOREIGN KEY (id_trenera) REFERENCES Treneri(id_trenera)
)
''')

def ievadit_sportistu():
    vards = input("Ievadiet sportista vārdu: ")
    uzvards = input("Ievadiet sportista uzvārdu: ")
    dzimšanas_gads = int(input("Ievadiet sportista dzimšanas gadu: "))
    talrunis = input("Ievadiet sportista tālruņa numuru: ")
    pilsēta = input("Ievadiet sportista pilsētu: ")

    cursor.execute("INSERT INTO Sportisti (vards, uzvards, dzimšanas_gads, talrunis, pilsēta) VALUES (?, ?, ?, ?, ?)", 
                   (vards, uzvards, dzimšanas_gads, talrunis, pilsēta))
    conn.commit()
    print("Sportists pievienots datubāzei.")

def ievadit_treneri():
    vards = input("Ievadiet trenera vārdu: ")
    uzvards = input("Ievadiet trenera uzvārdu: ")
    izglītība = input("Ievadiet trenera izglītību: ")
    kvalifikācija = input("Ievadiet trenera kvalifikāciju: ")

    cursor.execute("INSERT INTO Treneri (vards, uzvards, izglītība, kvalifikācija) VALUES (?, ?, ?, ?)", 
                   (vards, uzvards, izglītība, kvalifikācija))
    conn.commit()
    print("Treneris pievienots datubāzei.")    


def ievadit_apmeklējumu():
    id_sportista = int(input("Ievadiet sportista ID: "))
    id_trenera = int(input("Ievadiet trenera ID: "))
    datums = input("Ievadiet apmeklējuma datumu (YYYY-MM-DD): ")
    nodarbiibas_saakums = input("Ievadiet nodarbības sākuma laiku (HH:MM): ")
    nodarbiibas_beigas = input("Ievadiet nodarbības beigu laiku (HH:MM): ")

    from datetime import datetime
    laiks_sakums = datetime.strptime(nodarbiibas_saakums, "%H:%M")
    laiks_beigas = datetime.strptime(nodarbiibas_beigas, "%H:%M")
    laiks = int((laiks_beigas - laiks_sakums).total_seconds() / 60)

    cursor.execute("INSERT INTO Apmekleejumi (id_sportista, id_trenera, datums, nodarbiibas_saakums, nodarbiibas_beigas, laiks) VALUES (?, ?, ?, ?, ?, ?)", 
                   (id_sportista, id_trenera, datums, nodarbiibas_saakums, nodarbiibas_beigas, laiks))
    conn.commit()
    print("Apmeklējums pievienots datubāzei.")

def main():
    while True:
        print("\nIzvēlieties darbību😊")
        print("1. Pievienot sportistu")
        print("2. Pievienot treneri")
        print("3. Pievienot apmeklējumu")
        print("4. Iziet")
        print("5. Informācija")
        print("6. Meklēt sportista")
        print("7. Dzēst sportista")

        
        izvēle = input("Ievadiet izvēli (1-4): ")

        if izvēle == '1':
            ievadit_sportistu()
        elif izvēle == '2':
            ievadit_treneri()
        elif izvēle == '3':
            ievadit_apmeklējumu()
        elif izvēle == '4':
            print("Iziet no programmas.")
            break
        elif izvēle == '5':
            info()
        elif izvēle == '6':
            meklēt_sportistu()
        elif izvēle == '7':
            dzest_sportistu()
        else:
            print("Nederīga izvēle, lūdzu mēģiniet vēlreiz.")
def info():
    cursor.execute("SELECT * FROM Sportisti")
    sportisti = cursor.fetchall()
    print("Sportisti😊")
    for sportists in sportisti:
        print(sportists)

    cursor.execute("SELECT * FROM Treneri")
    treneri = cursor.fetchall()
    print("\nTreneri😊")
    for treneris in treneri:
        print(treneris)

    cursor.execute("SELECT * FROM Apmekleejumi")
    apmeklejumi = cursor.fetchall()
    print("\nApmeklējumi😊")
    for apmeklejumus in apmeklejumi:
        print(apmeklejumus)
        

def meklēt_sportistu():
    meklējums = input("Ievadiet sportista vārdu vai uzvārdu, ko meklēt: ")
    cursor.execute("SELECT * FROM Sportisti WHERE vards LIKE ? OR uzvards LIKE ?", 
                   (f"%{meklējums}%", f"%{meklējums}%"))
    rezultati = cursor.fetchall()
    
    if rezultati:
        print("\nAtrastie sportisti😊")
        for sportists in rezultati:
            print(f"ID: {sportists[0]}, Vārds: {sportists[1]}, Uzvārds: {sportists[2]}, Dzimšanas gads: {sportists[3]}, Tālrunis: {sportists[4]}, Pilsēta: {sportists[5]}")
    else:
        print("Netika atrasts neviens sportists ar ievadīto vārdu vai uzvārdu.")

def dzest_sportistu():
    try:
        id_sportista = int(input("Ievadiet sportista ID, kuru vēlaties dzēst: "))
        
        # Pārbaudām, vai sportists eksistē
        cursor.execute("SELECT * FROM Sportisti WHERE id_sportista = ?", (id_sportista,))
        sportists = cursor.fetchone()
        
        if sportists:
            print(f"Jūs dzēsīsiet sportistu: ID={sportists[0]}, Vārds={sportists[1]}, Uzvārds={sportists[2]}")
            apstiprinajums = input("Vai tiešām vēlaties dzēst šo sportistu? (j/n): ")
            if apstiprinajums.lower() == 'j':
                cursor.execute("DELETE FROM Sportisti WHERE id_sportista = ?", (id_sportista,))
                conn.commit()
                print("Sportists veiksmīgi dzēsts no datubāzes.")
            else:
                print("Darbība atcelta.")
        else:
            print("Sportists ar norādīto ID netika atrasts.")
    except ValueError:
        print("Lūdzu ievadiet derīgu ID skaitli.")

main() 