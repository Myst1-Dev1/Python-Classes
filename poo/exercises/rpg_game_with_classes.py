import random


# ---------- Classe base ----------
class Personagem:
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
        print(f"{self.nome} ataca {alvo.nome} e causa {dano} de dano!")

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)

    def __str__(self):
        return f"{self.nome} [{self.vida}/{self.vida_max} HP]"


# ---------- Herança: classes de herói ----------
class Heroi(Personagem):
    def __init__(self, nome, vida, ataque, defesa):
        super().__init__(nome, vida, ataque, defesa)
        self.nivel = 1
        self.xp = 0
        self.pocoes = 2

    def usar_pocao(self):
        if self.pocoes <= 0:
            print("Você não tem poções!")
            return False
        cura = 30
        self.vida = min(self.vida_max, self.vida + cura)
        self.pocoes -= 1
        print(f"{self.nome} usa uma poção e recupera {cura} HP! (restam {self.pocoes})")
        return True

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        print(f"{self.nome} ganhou {quantidade} XP!")
        while self.xp >= self.nivel * 20:
            self.xp -= self.nivel * 20
            self.subir_nivel()

    def subir_nivel(self):
        self.nivel += 1
        self.vida_max += 10
        self.vida = self.vida_max
        self.ataque += 2
        self.defesa += 1
        print(f"*** {self.nome} subiu para o nível {self.nivel}! ***")

    def habilidade_especial(self, alvo):
        raise NotImplementedError("Cada classe define a sua habilidade")


class Guerreiro(Heroi):
    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque=12, defesa=5)

    def habilidade_especial(self, alvo):
        dano = self.ataque * 2 - alvo.defesa
        alvo.receber_dano(dano)
        print(f"{self.nome} usa GOLPE PODEROSO em {alvo.nome}: {dano} de dano!")


class Mago(Heroi):
    def __init__(self, nome):
        super().__init__(nome, vida=70, ataque=8, defesa=2)
        self.mana = 30

    def habilidade_especial(self, alvo):
        if self.mana < 10:
            print("Mana insuficiente! Ataque normal no lugar.")
            return self.atacar(alvo)
        self.mana -= 10
        dano = self.ataque * 3  # ignora defesa
        alvo.receber_dano(dano)
        print(f"{self.nome} lança BOLA DE FOGO em {alvo.nome}: {dano} de dano! (mana: {self.mana})")


class Arqueiro(Heroi):
    def __init__(self, nome):
        super().__init__(nome, vida=80, ataque=10, defesa=3)

    def habilidade_especial(self, alvo):
        print(f"{self.nome} dispara CHUVA DE FLECHAS!")
        for _ in range(3):
            self.atacar(alvo)
            if not alvo.vivo:
                break


# ---------- Inimigos ----------
class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, defesa, xp_recompensa):
        super().__init__(nome, vida, ataque, defesa)
        self.xp_recompensa = xp_recompensa


def criar_inimigo(nivel_heroi):
    tipos = [
        ("Goblin", 30, 7, 1, 10),
        ("Orc", 50, 10, 3, 18),
        ("Esqueleto", 40, 9, 2, 14),
    ]
    nome, vida, atq, defesa, xp = random.choice(tipos)
    escala = nivel_heroi - 1
    return Inimigo(nome, vida + escala * 8, atq + escala * 2, defesa + escala, xp)


# ---------- Jogo ----------
def batalha(heroi, inimigo):
    print(f"\n⚔️  Um {inimigo.nome} selvagem apareceu!")
    while heroi.vivo and inimigo.vivo:
        print(f"\n{heroi}  vs  {inimigo}")
        escolha = input("[1] Atacar  [2] Especial  [3] Poção  [4] Fugir > ").strip()

        if escolha == "1":
            heroi.atacar(inimigo)
        elif escolha == "2":
            heroi.habilidade_especial(inimigo)
        elif escolha == "3":
            if not heroi.usar_pocao():
                continue
        elif escolha == "4":
            if random.random() < 0.5:
                print("Você fugiu!")
                return
            print("Não conseguiu fugir!")
        else:
            print("Opção inválida.")
            continue

        if inimigo.vivo:
            inimigo.atacar(heroi)

    if heroi.vivo:
        print(f"\n🏆 Você derrotou o {inimigo.nome}!")
        heroi.ganhar_xp(inimigo.xp_recompensa)
        if random.random() < 0.4:
            heroi.pocoes += 1
            print("O inimigo deixou cair uma poção!")


def escolher_heroi():
    classes = {"1": Guerreiro, "2": Mago, "3": Arqueiro}
    nome = input("Nome do seu herói: ").strip() or "Herói"
    while True:
        op = input("Classe: [1] Guerreiro  [2] Mago  [3] Arqueiro > ").strip()
        if op in classes:
            return classes[op](nome)
        print("Opção inválida.")


def main():
    heroi = escolher_heroi()
    print(f"\nBem-vindo, {heroi.nome}, o {type(heroi).__name__}!")

    while heroi.vivo:
        batalha(heroi, criar_inimigo(heroi.nivel))
        if heroi.vivo and input("\nContinuar a aventura? (s/n) > ").lower() != "s":
            break

    if not heroi.vivo:
        print("\n💀 Fim de jogo...")
    else:
        print(f"\nVocê encerrou a aventura no nível {heroi.nivel}. Até a próxima!")


if __name__ == "__main__":
    main()