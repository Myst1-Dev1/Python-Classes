import random
import tkinter as tk

BG = "#1e1e2e"


def saida(msg):
    """Por padrão imprime no terminal; a janela troca isso por escrever no log."""
    print(msg)


# ---------- Classe base ----------
class Personagem:
    icone = "❓"

    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.vida_max = vida
        self.ataque = ataque
        self.defesa = defesa

    @property
    def vivo(self):
        return self.vida > 0

    def atacar(self, alvo):
        dano = max(1, self.ataque + random.randint(-2, 3) - alvo.defesa)
        alvo.receber_dano(dano)
        saida(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano!")

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)


# ---------- Heróis ----------
class Heroi(Personagem):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.nivel = 1
        self.xp = 0
        self.pocoes = 2

    def usar_pocao(self):
        if self.pocoes <= 0:
            saida("Você não tem poções!")
            return False
        self.vida = min(self.vida_max, self.vida + 30)
        self.pocoes -= 1
        saida(f"{self.nome} usa uma poção e recupera 30 HP!")
        return True

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        saida(f"{self.nome} ganhou {quantidade} XP!")
        while self.xp >= self.nivel * 20:
            self.xp -= self.nivel * 20
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.vida_max += 10
        self.vida = self.vida_max
        self.ataque += 2
        self.defesa += 1
        saida(f"*** {self.nome} subiu para o nível {self.nivel}! ***")

    def habilidade_especial(self, alvo):
        raise NotImplementedError


class Guerreiro(Heroi):
    icone = "⚔️"

    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque=12, defesa=5)

    def habilidade_especial(self, alvo):
        dano = self.ataque * 2 - alvo.defesa
        alvo.receber_dano(dano)
        saida(f"{self.nome} usa GOLPE PODEROSO: {dano} de dano!")


class Mago(Heroi):
    icone = "🧙"

    def __init__(self, nome):
        super().__init__(nome, vida=70, ataque=8, defesa=2)
        self.mana = 30

    def habilidade_especial(self, alvo):
        if self.mana < 10:
            saida("Mana insuficiente! Ataque normal no lugar.")
            return self.atacar(alvo)
        self.mana -= 10
        dano = self.ataque * 3
        alvo.receber_dano(dano)
        saida(f"{self.nome} lança BOLA DE FOGO: {dano} de dano!")


class Arqueiro(Heroi):
    icone = "🏹"

    def __init__(self, nome):
        super().__init__(nome, vida=80, ataque=10, defesa=3)

    def habilidade_especial(self, alvo):
        saida(f"{self.nome} dispara CHUVA DE FLECHAS!")
        for _ in range(3):
            self.atacar(alvo)
            if not alvo.vivo:
                break


# ---------- Inimigos ----------
class Inimigo(Personagem):
    def __init__(self, nome, icone, vida, ataque, defesa, xp_recompensa):
        super().__init__(nome, vida, ataque, defesa)
        self.icone = icone
        self.xp_recompensa = xp_recompensa


def criar_inimigo(nivel_heroi):
    tipos = [
        ("Goblin", "👺", 30, 7, 1, 10),
        ("Orc", "👹", 50, 10, 3, 18),
        ("Esqueleto", "💀", 40, 9, 2, 14),
    ]
    nome, icone, vida, atq, defesa, xp = random.choice(tipos)
    e = nivel_heroi - 1
    return Inimigo(nome, icone, vida + e * 8, atq + e * 2, defesa + e, xp)


# ---------- Janela do jogo ----------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        global saida
        saida = self.escrever
        self.title("RPG em Python")
        self.configure(bg=BG)
        self.resizable(False, False)
        self.heroi = None
        self.inimigo = None
        self.travado = False
        self.tela_inicial()

    def limpar(self):
        for w in self.winfo_children():
            w.destroy()

    # ----- tela de escolha -----
    def tela_inicial(self):
        self.limpar()
        tk.Label(self, text="⚔️ RPG em Python", font=("Arial", 24, "bold"),
                 bg=BG, fg="white").pack(padx=60, pady=(20, 10))
        tk.Label(self, text="Nome do herói:", bg=BG, fg="white").pack()
        self.entrada = tk.Entry(self, font=("Arial", 14), justify="center")
        self.entrada.insert(0, "Herói")
        self.entrada.pack(pady=5)
        frame = tk.Frame(self, bg=BG)
        frame.pack(pady=15, padx=20)
        for classe in (Guerreiro, Mago, Arqueiro):
            tk.Button(frame, text=f"{classe.icone}\n{classe.__name__}",
                      font=("Arial", 14), width=10, height=3,
                      command=lambda c=classe: self.iniciar(c)).pack(side="left", padx=8)

    def iniciar(self, classe):
        self.heroi = classe(self.entrada.get().strip() or "Herói")
        self.tela_batalha()
        self.novo_inimigo()

    # ----- tela de batalha -----
    def tela_batalha(self):
        self.limpar()
        self.canvas = tk.Canvas(self, width=600, height=250, bg="#2a2a40", highlightthickness=0)
        self.canvas.pack(padx=10, pady=10)
        self.info = tk.Label(self, bg=BG, fg="#cdd6f4", font=("Arial", 11))
        self.info.pack()

        botoes = tk.Frame(self, bg=BG)
        botoes.pack(pady=8)
        for texto, acao in [("Atacar", "atacar"), ("Especial", "especial"),
                            ("Poção", "pocao"), ("Fugir", "fugir")]:
            tk.Button(botoes, text=texto, width=10, font=("Arial", 12),
                      command=lambda a=acao: self.acao(a)).pack(side="left", padx=5)

        self.log = tk.Text(self, height=8, width=70, state="disabled",
                           bg="#11111b", fg="#a6e3a1", font=("Courier", 10))
        self.log.pack(padx=10, pady=(0, 10))

    def escrever(self, msg):
        self.log.config(state="normal")
        self.log.insert("end", msg + "\n")
        self.log.see("end")
        self.log.config(state="disabled")

    def barra(self, x, personagem):
        c = self.canvas
        pct = personagem.vida / personagem.vida_max
        cor = "#a6e3a1" if pct > 0.5 else "#f9e2af" if pct > 0.25 else "#f38ba8"
        c.create_text(x, 160, text=personagem.nome, fill="white", font=("Arial", 13, "bold"))
        c.create_rectangle(x - 80, 180, x + 80, 196, fill="#45475a", outline="")
        c.create_rectangle(x - 80, 180, x - 80 + 160 * pct, 196, fill=cor, outline="")
        c.create_text(x, 208, text=f"{personagem.vida}/{personagem.vida_max} HP",
                      fill="white", font=("Arial", 10))

    def desenhar(self):
        c = self.canvas
        c.delete("all")
        c.create_text(150, 90, text=self.heroi.icone, font=("Arial", 64))
        c.create_text(450, 90, text=self.inimigo.icone, font=("Arial", 64))
        c.create_text(300, 90, text="VS", fill="#6c7086", font=("Arial", 20, "bold"))
        self.barra(150, self.heroi)
        self.barra(450, self.inimigo)
        h = self.heroi
        extra = f" | Mana: {h.mana}" if hasattr(h, "mana") else ""
        self.info.config(text=f"Nível {h.nivel} | XP {h.xp}/{h.nivel * 20} | Poções: {h.pocoes}{extra}")

    # ----- lógica dos turnos -----
    def novo_inimigo(self):
        self.inimigo = criar_inimigo(self.heroi.nivel)
        saida(f"\nUm {self.inimigo.nome} selvagem apareceu!")
        self.travado = False
        self.desenhar()

    def acao(self, tipo):
        if self.travado:
            return
        h, i = self.heroi, self.inimigo
        if tipo == "atacar":
            h.atacar(i)
        elif tipo == "especial":
            h.habilidade_especial(i)
        elif tipo == "pocao":
            if not h.usar_pocao():
                return
        elif tipo == "fugir":
            if random.random() < 0.5:
                saida("Você fugiu!")
                return self.novo_inimigo()
            saida("Não conseguiu fugir!")

        self.desenhar()
        if not i.vivo:
            return self.vitoria()
        self.travado = True
        self.after(600, self.turno_inimigo)

    def turno_inimigo(self):
        self.inimigo.atacar(self.heroi)
        self.desenhar()
        if self.heroi.vivo:
            self.travado = False
        else:
            self.fim()

    def vitoria(self):
        self.travado = True
        saida(f"Você derrotou o {self.inimigo.nome}!")
        self.heroi.ganhar_xp(self.inimigo.xp_recompensa)
        if random.random() < 0.4:
            self.heroi.pocoes += 1
            saida("O inimigo deixou cair uma poção!")
        self.desenhar()
        self.after(1500, self.novo_inimigo)

    def fim(self):
        self.travado = True
        self.canvas.create_text(300, 125, text="GAME OVER", fill="#f38ba8",
                                font=("Arial", 40, "bold"))
        tk.Button(self, text="Jogar de novo", font=("Arial", 12),
                  command=self.tela_inicial).pack(pady=(0, 10))


if __name__ == "__main__":
    App().mainloop()