import tkinter as tk
def difference():
    x = float(entry_x.get())
    y = float(entry_y.get())
    
    difference = x - y
    result_label.config(text=f"La difference de deux nombre est : {difference}")

root = tk.Tk()
root.title("Calculatrice Difference")
root.geometry("500x600")


label_x = tk.Label(root, text="Entrez la premier nombre :")
label_x.pack()
entry_x = tk.Entry(root)
entry_x.pack()

label_y = tk.Label(root, text="Entrez la deuxieme nombre:")
label_y.pack()
entry_y = tk.Entry(root)
entry_y.pack()

calculate_button = tk.Button(root, text="Click ici Pour le resulat :", command=difference)
calculate_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

labeldefault = tk.Label(root,text="Developed by LAMGAMATE SALAH EDDINE",bg="yellow",font="65")
labeldefault.pack(side="bottom")
root.mainloop()
