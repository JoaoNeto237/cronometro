from tkinter import *


cor1 = '#0a0a0a' #preto
cor2 = '#fafcff' #branco
cor3 = '#21c25c' #verde
cor4 = '#eb463b' #vermelho
cor5 = '#dedcdc' #cinza
cor6 = '#3080f0' #azul


janela = Tk()
janela.geometry('300x180')
janela.title("")
janela.configure(bg=cor1)
janela.resizable(width=FALSE, height=FALSE)


global temp
global limitador
global cont
global run


limitador = 59
temp = "00:00:00"
run = False
cont = -5

def iniciar():
    global temp
    global cont
    global limitador


    if run :

        if cont <= -1:
            inicio = 'Comecando em ' + str(cont)
            lb_tempo['text'] = inicio
            lb_tempo['font'] = 'Arial 10'

        else:
            lb_tempo['font'] = 'Times 50 bold'
            temporario = str(temp)
            h,m,s = map(int, temporario.split(":"))
            h = int(h)
            m = int(m)
            s = int(cont)

            if (s >= limitador):
                cont = 0
                m+=1

            s = str(0)+str(s)
            m = str(0)+str(m)
            h = str(0)+str(h)

            temporario = str(h[-2:])+":"+str(m[-2:])+":"+str(s[-2:])
            lb_tempo['text'] = temporario
            temp = temporario


        lb_tempo.after(1000, iniciar)
        cont += 1



def start():
    global run
    run = True
    iniciar() 


def pausar():
    global run
    run = False
    

def reiniciar():
    global cont
    global temp


    cont = 0


    temp = "00:00:00"
    lb_tempo['text'] = temp
    


app = Label(janela, text="Cronômetro", bg=cor1, fg=cor2, font=('Arial 10'))
app.place(x=20, y=5)
lb_tempo = Label(janela, text=temp, bg=cor1, fg=cor3, font=('Times  50 bold'))
lb_tempo.place(x=20, y=35)

inic = Button(janela,command=start, text="Iniciar", width=8, height=1,relief='raised', overrelief='ridge', bg=cor1, fg=cor5, font=('Arial 13'))
inic.place(x=20 ,y=130)
pausar = Button(janela,command=pausar, text="Pausar", width=8, height=1, relief='raised', overrelief='ridge',bg=cor1, fg=cor5, font=('Arial 13'))
pausar.place(x=105 ,y=130)
reiniciar = Button(janela,command=reiniciar, text="Reiniciar", width=8, height=1, relief='raised', overrelief='ridge', bg=cor1, fg=cor5, font=('Arial 13'))
reiniciar.place(x=190 ,y=130)


janela.mainloop()