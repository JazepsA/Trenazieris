import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('trenazieru_zale.db')
cursor = conn.cursor()

def pievienot_sportistu():
    def saglabat_sportistu():
        vards = vards_entry.get()
        uzvards = uzvards_entry.get()
        dzimsanas_gads = dzimsanas_gads_entry.get()
        talrunis = talrunis_entry.get()
        pilseta = pilseta_entry.get()

        if vards and uzvards and dzimsanas_gads.isdigit():
            cursor.execute(
                "INSERT INTO Sportisti (vards, uzvards, dzimšanas_gads, talrunis, pilsēta) VALUES (?, ?, ?, ?, ?)",
                (vards, uzvards, int(dzimsanas_gads), talrunis, pilseta)
            )
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Sportists pievienots!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot sportistu")
    logs.geometry("300x300")

    tk.Label(logs, text="Vārds:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    tk.Label(logs, text="Uzvārds:").pack()
    uzvards_entry = tk.Entry(logs)
    uzvards_entry.pack()

    tk.Label(logs, text="Dzimšanas gads:").pack()
    dzimsanas_gads_entry = tk.Entry(logs)
    dzimsanas_gads_entry.pack()

    tk.Label(logs, text="Tālrunis:").pack()
    talrunis_entry = tk.Entry(logs)
    talrunis_entry.pack()

    tk.Label(logs, text="Pilsēta:").pack()
    pilseta_entry = tk.Entry(logs)
    pilseta_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_sportistu)
    saglabat_btn.pack(pady=10)


def meklēt_sportistu():
    def atrast_sportistu():
        vards = vards_entry.get()
        if vards:
            cursor.execute("SELECT * FROM Sportisti WHERE vards LIKE ?", (f"%{vards}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}, {r[4]}, {r[5]}\n"
            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens sportists.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet sportista vārdu!")

    logs = tk.Toplevel()
    logs.title("Meklēt sportistu")
    logs.geometry("300x200")

    tk.Label(logs, text="Sportista vārds:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_sportistu)
    meklēt_btn.pack(pady=10)


def dzēst_sportistu():
    def dzēst_sportistu_no_db():
        id_sportista = id_sportista_entry.get()
        if id_sportista.isdigit():
            cursor.execute("DELETE FROM Sportisti WHERE id_sportista = ?", (id_sportista,))
            conn.commit()
            messagebox.showinfo("Veiksmīgi", f"Sportists ar ID {id_sportista} tika izdzēsts!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet derīgu ID!")

    logs = tk.Toplevel()
    logs.title("Dzēst sportistu")
    logs.geometry("300x150")

    tk.Label(logs, text="Sportista ID:").pack()
    id_sportista_entry = tk.Entry(logs)
    id_sportista_entry.pack()

    dzēst_btn = tk.Button(logs, text="Dzēst", command=dzēst_sportistu_no_db)
    dzēst_btn.pack(pady=10)


def sportistu_logs():
    sportisti_logs = tk.Toplevel()
    sportisti_logs.title("Sportistu pārvaldība")
    sportisti_logs.geometry("300x250")

    pievienot_btn = tk.Button(sportisti_logs, text="Pievienot sportistu", command=pievienot_sportistu, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(sportisti_logs, text="Meklēt sportistu", command=meklēt_sportistu, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(sportisti_logs, text="Dzēst sportistu", command=dzēst_sportistu, width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(sportisti_logs, text="Iziet", command=sportisti_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)

def pievienot_treneri():
    def saglabat_treneri():
        vards = vards_entry.get()
        uzvards = uzvards_entry.get()
        izglītība = izglitiba_entry.get()
        kvalifikācija = kvalifikacija_entry.get()

        if vards and uzvards and kvalifikācija:
            cursor.execute(
                "INSERT INTO Treneri (vards, uzvards, izglītība, kvalifikācija) VALUES (?, ?, ?, ?)",
                (vards, uzvards, izglītība, kvalifikācija)
            )
            conn.commit()
            messagebox.showinfo("Veiksmīgi", "Treneris pievienots!")
            logs.destroy()
        else:
            messagebox.showerror("Kļūda", "Lūdzu, aizpildiet visus laukus korekti!")

    logs = tk.Toplevel()
    logs.title("Pievienot treneri")
    logs.geometry("300x300")

    tk.Label(logs, text="Vārds:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    tk.Label(logs, text="Uzvārds:").pack()
    uzvards_entry = tk.Entry(logs)
    uzvards_entry.pack()

    tk.Label(logs, text="Kvalifikācija:").pack()
    kvalifikacija_entry = tk.Entry(logs)
    kvalifikacija_entry.pack()

    tk.Label(logs, text="Izglītība:").pack()
    izglitiba_entry = tk.Entry(logs)
    izglitiba_entry.pack()

    saglabat_btn = tk.Button(logs, text="Saglabāt", command=saglabat_treneri)
    saglabat_btn.pack(pady=10)

def meklēt_treneri():
    def atrast_treneri():
        vards = vards_entry.get()
        if vards:
            cursor.execute("SELECT * FROM Treneri WHERE vards LIKE ?", (f"%{vards}%",))
            rezultati = cursor.fetchall()
            if rezultati:
                rezultati_str = ""
                for r in rezultati:
                    rezultati_str += f"{r[0]}: {r[1]} {r[2]}, {r[3]}, {r[4]}\n"
                    messagebox.showinfo("Atbilde",f"{r[1]} ,tāds treneris ir mūsu datubāzē!")

            else:
                messagebox.showinfo("Rezultāti", "Netika atrasts neviens treneris.")
        else:
            messagebox.showerror("Kļūda", "Lūdzu, ievadiet sportista vārdu!")

    logs = tk.Toplevel()
    logs.title("Meklēt treneri")
    logs.geometry("300x200")

    tk.Label(logs, text="Trenera vārds:").pack()
    vards_entry = tk.Entry(logs)
    vards_entry.pack()

    meklēt_btn = tk.Button(logs, text="Meklēt", command=atrast_treneri)
    meklēt_btn.pack(pady=10)


def treneru_logs():
    treneri_logs = tk.Toplevel()
    treneri_logs.title("Sportistu pārvaldība")
    treneri_logs.geometry("300x250")

    pievienot_btn = tk.Button(treneri_logs, text="Pievienot treneri", command=pievienot_treneri, width=25, height=2, bg="lightblue")
    pievienot_btn.pack(pady=10)

    meklēt_btn = tk.Button(treneri_logs, text="Meklēt treneri",command=meklēt_treneri, width=25, height=2, bg="lightgreen")
    meklēt_btn.pack(pady=10)

    dzēst_btn = tk.Button(treneri_logs, text="Dzēst treneri", width=25, height=2, bg="lightyellow")
    dzēst_btn.pack(pady=10)

    iziet_btn = tk.Button(treneri_logs, text="Iziet", command=treneri_logs.destroy, width=25, height=2, bg="red", fg="white")
    iziet_btn.pack(pady=10)

def izveidot_galveno_logu():
    def sportisti_poga():
        sportistu_logs()

    def treneri_poga():
        treneru_logs()

    def apmeklejumi_poga():
        messagebox.showinfo("Apmeklējumi", "Atvērta apmeklējumu pārvaldība.")

    logs = tk.Tk()
    logs.title("Trenažieru zāles pārvaldība")
    logs.geometry("300x200")

    sportisti_btn = tk.Button(logs, text="Sportisti", command=sportisti_poga, width=20, height=2, bg="lightblue")
    sportisti_btn.pack(pady=10)

    treneri_btn = tk.Button(logs, text="Treneri", command=treneri_poga, width=20, height=2, bg="lightgreen")
    treneri_btn.pack(pady=10)

    apmeklejumi_btn = tk.Button(logs, text="Apmeklējumi", command=apmeklejumi_poga, width=20, height=2, bg="lightyellow")
    apmeklejumi_btn.pack(pady=10)

    logs.mainloop()


if __name__ == "__main__":
    izveidot_galveno_logu()