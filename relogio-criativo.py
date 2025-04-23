import tkinter as tk
import time

#Função que atualiza  a hora 
def atualizar_hora():
  hora_atual = time.strftime("%H:%M:%S") # Formato da hora
  rotulo_hora.config(text=hora_atual)
  janela.after(1000, atualizar_hora) # atualizar a cada 1000ms(1 segundo)

#Criando a janela principal
janela = tk.Tk()
janela.title("Relógio Digital 🕒")
janela.geometry("300x100")
janela.configure(bg="#0d4f7b") # fundo escuro


# Criando  rótulo que mostra a hora
rotulo_hora = tk.Label(janela, font=("Helvetica", 36), fg="#ce12ea", bg="#0d4f7b")
rotulo_hora.pack(pady=20)

#iniciar atualização da hora
atualizar_hora()

#Mostra a janela
janela.mainloop()
