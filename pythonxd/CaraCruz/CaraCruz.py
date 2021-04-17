import random
from tkinter import *
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = Tk()
root.title("Cara o Cruz")
num = random.randint(1, 13)

probability = 0
thrown = 0
heads = 0
tails = 0
data = {"index": [],
        "prob": []
        }


# Funcion para reciclar Widgets obsoletos
def clear():
    list = root.grid_slaves()
    for l in list:
        if not "button" in str(l):
            l.destroy()


# Función que "lanza" una moneda y actualiza los datos

def ClickButton():
    # Borramos los widgets preexistentes para no sobrecargar el programa
    clear()

    # Declaramos las variables localmente para poder alterarlas desde la función
    global probability
    global thrown
    global heads
    global tails
    global data

    # Busco un número aleatorio entre 1 y 2 de forma que hay un 50% de que salga cara
    num = random.randint(1, 2)
    if num == 1:
        foto = "cara.PNG"
        heads += 1
    else:
        foto = "cruz.PNG"
        tails += 1

    # Actualizamos las variables y el y el diccionario data para hacer la gráfica
    thrown += 1
    probability = (heads / thrown)
    data["index"].append(thrown)
    data["prob"].append(probability)

    # Widget imagen
    img1 = Image.open(foto)
    img1 = img1.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img1)
    imglabel = Label(image=img)
    imglabel.image = img
    imglabel.grid_forget()
    imglabel.grid(row=1, column=0, columnspan=2)

    # Widget contador cara y cruz
    countlabel = Label(text="Cara: " + str(heads) + "\nCruz: " + str(tails), font="Arial", padx=40, pady=20)
    countlabel.grid_forget()
    countlabel.grid(row=2, column=0, columnspan=2)

    # Widget probabilidad
    problabel = Label(
        text="Veces lanzada: " + str(thrown) + "\nProbabilidad de caras: {:.8f}".format(probability) + "%",
        font="Arial", padx=40, pady=20)
    problabel.grid_forget()
    problabel.grid(row=3, column=0, columnspan=2)


# Función que ejecuta ClickButton 50 veces, para ir mas rapido
def ClickButton50():
    for i in range(50):
        ClickButton()


# Gráfica
def Plot():
    global data
    df = pd.DataFrame(data, columns=['index', 'prob'])

    figure = plt.Figure(figsize=(6, 5), dpi=100)
    ax = figure.add_subplot(1, 1, (0, 1))
    chart_type = FigureCanvasTkAgg(figure, root)
    chart_type.get_tk_widget().grid(row=1, column=2, rowspan=3)
    df = df[['index', 'prob']].groupby('index').sum()
    df.plot(kind='line', legend=True, ax=ax)
    ax.set_title('Gráfico de probabilidad')


# Declaración y posicionamiento de los botones en el grid

button1 = Button(root, text="Lanza la moneda", font="Arial", padx=40, pady=20, command=ClickButton, bg="#7EB6E8")
button1.grid(row=0, column=0)

button2 = Button(root, text="Lanza 50 veces", font="Arial", padx=40, pady=20, command=ClickButton50, bg="#7EB6E8")
button2.grid(row=0, column=1)

button3 = Button(root, text="Actualiza la gráfica", font="Arial", padx=40, pady=20, command=Plot, bg="#7EB6E8")
button3.grid(row=0, column=2)

root.mainloop()
