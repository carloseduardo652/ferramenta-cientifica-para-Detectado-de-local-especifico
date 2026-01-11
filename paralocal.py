import tkinter as tk
from tkinter import messagebox
import random

class DetectorLocal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ferramenta Científica para Detectado de Local")
        self.root.geometry("800x700")

        # Base de dados baseada nos casos 01, 02, 03 e 04
        self.dados_locais = {
            "Futebol": [
                "Movimento — 10–13 km/jogo", "Deslocamento — ≈ 50 m", "Trajetória — 40–60 m",
                "Velocidade — Jogador: até 36 km/h | Bola: 90–120 km/h", "Aceleração — ≈ 4 m/s²",
                "Movimento parabólico — 30°–45°", "Inércia — 65–90 kg", "Força aplicada — ≈ 1000 N",
                "Ação e reação — ≈ 1000 N", "Força gravitacional — 700–900 N", "Força normal — 700–900 N",
                "Força elástica — deformação em ms", "Impulso — 10–20 N·s", "Atrito — 0,6–0,8",
                "Energia cinética — 100–150 J", "Energia potencial gravitacional — 20–50 J",
                "Transformação de energia — 800–1200 kcal", "Movimento rotacional — 50–100 rad/s",
                "Propagação do som no ar — 343 m/s", "Intensidade sonora — 100–120 dB",
                "Trocas térmicas por evaporação — 1–3 L", "Produção de calor metabólico — 800–1200 kcal",
                "Arrasto do ar — 0,1–1 N", "Turbulência do ar — ≈ 10⁵", "Respiração celular — 60–75 mL/kg/min",
                "Equilíbrio ácido–base — pH 7,4", "Liberação de neurotransmissores — ↑ nmol/L"
            ],
            "Padaria": [
                "Temperatura — 180–250 °C", "Calor — 2–4 MJ", "Transferência de calor — 5–10 kW",
                "Condução térmica — 0,5–1,5 W/m·K", "Convecção — 1–3 m/s", "Radiação térmica — 5–20 kW/m²",
                "Dilatação térmica — 1–3 mm", "Pressão — 1 atm", "Força — 50–150 N", "Trabalho — 100–300 J",
                "Energia — 3–6 MJ", "Potência — 5–20 kW", "Atrito — 0,3–0,6", "Gravidade — 9,8 m/s²",
                "Massa — 0,5–1 kg", "Densidade — 0,2–0,4 g/cm³", "Volume — 1–2 L", "Viscosidade — 10³–10⁴ Pa·s",
                "Umidade — 60–80 %", "Mudança de estado físico — 100 °C", "Carbono — 45–50 %",
                "Hidrogênio — 6–7 %", "Oxigênio — 40–45 %", "Nitrogênio — 2–3 %", "Sódio — 1–2 %",
                "Cloro — 1–2 %", "Cálcio — 20–50 mg/100 g", "Ferro — 2–4 mg/100 g"
            ],
            "Sorveteria": [
                "Temperatura — −20 a −5 °C", "Calor — 1–3 MJ", "Transferência de calor — 2–8 kW",
                "Condução térmica — 0,4–1,0 W/m·K", "Convecção — 0,5–2 m/s", "Radiação térmica — 2–10 kW/m²",
                "Mudança de estado físico — 0 °C", "Solidificação — −5 a −10 °C", "Fusão — −2 a 0 °C",
                "Pressão — 1–2 atm", "Energia — 2–5 MJ", "Trabalho — 50–200 J", "Potência — 1–5 kW",
                "Atrito — 0,2–0,4", "Gravidade — 9,8 m/s²", "Massa — 0,1–1 kg", "Densidade — 0,5–0,7 g/cm³",
                "Volume — 0,1–1 L", "Viscosidade — 10²–10³ Pa·s", "Refrigeração — −20 °C", "Carbono — 40–50 %",
                "Hidrogênio — 6–8 %", "Oxigênio — 40–45 %", "Nitrogênio — 1–2 %", "Sódio — 30–80 mg/100 g",
                "Cálcio — 100–150 mg/100 g", "Potássio — 150–250 mg/100 g", "Fósforo — 80–120 mg/100 g",
                "Enxofre — 0,1–0,3 %", "Magnésio — 10–30 mg/100 g"
            ],
            "Piscina": [
                "Flutuação — 0,98–1,02 g/cm³", "Empuxo — 600–800 N", "Densidade — 1,0 g/cm³",
                "Pressão hidrostática — 1,2 atm", "Volume — 50–500 m³", "Massa — 1000 kg/m³",
                "Gravidade — 9,8 m/s²", "Força — 200–600 N", "Aceleração — 1–3 m/s²", "Velocidade — 1–2 m/s",
                "Resistência do fluido — 10–100 N", "Atrito — 0,02–0,05", "Tensão superficial — 0,072 N/m",
                "Capilaridade — 1–5 mm", "Temperatura — 26–30 °C", "Calor — 10–50 MJ",
                "Transferência de calor — 5–20 kW", "Dilatação térmica — 0,2 %", "Ondas — 0,5–2 Hz",
                "Refração — 1,33", "Hidrogênio — 11 %", "Oxigênio — 89 %", "Cloro — 1–3 ppm",
                "Sódio — 10–50 mg/L", "Cálcio — 200–400 ppm", "Carbono — 1–5 ppm", "Nitrogênio — < 1 ppm",
                "Magnésio — 10–50 ppm"
            ]
        }

        self.selecionados = []
        self.todas_opcoes = []
        for local in self.dados_locais:
            self.todas_opcoes.extend(self.dados_locais[local])
        
        # Remover duplicatas e misturar
        self.todas_opcoes = list(set(self.todas_opcoes))
        random.shuffle(self.todas_opcoes)

        self.setup_ui()

    def setup_ui(self):
        # Instruções e Contador
        self.label_instrucao = tk.Label(self.root, text="Escolha o mais importante ao local específico que deseja encontrar", font=("Arial", 12, "bold"))
        self.label_instrucao.pack(pady=10)

        self.label_contador = tk.Label(self.root, text="Faltam 10 escolhas", font=("Arial", 10))
        self.label_contador.pack()

        # Frame com Scrollbar para listar as opções
        frame_lista = tk.Frame(self.root)
        frame_lista.pack(expand=True, fill="both", padx=20, pady=10)

        self.canvas = tk.Canvas(frame_lista)
        scrollbar = tk.Scrollbar(frame_lista, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side="left", expand=True, fill="both")
        scrollbar.pack(side="right", fill="y")

        # Criar botões para cada opção
        for opcao in self.todas_opcoes:
            btn = tk.Button(self.scrollable_frame, text=opcao, width=80, anchor="w",
                            command=lambda opt=opcao: self.selecionar_opcao(opt))
            btn.pack(pady=2, padx=5)

    def selecionar_opcao(self, opcao):
        if len(self.selecionados) < 10:
            if opcao not in self.selecionados:
                self.selecionados.append(opcao)
                restantes = 10 - len(self.selecionados)
                self.label_contador.config(text=f"Faltam {restantes} escolhas")
                
                if len(self.selecionados) == 10:
                    self.calcular_resultado()
            else:
                messagebox.showinfo("Aviso", "Você já selecionou esta opção.")
        else:
            messagebox.showwarning("Limite atingido", "Você já selecionou as 10 informações.")

    def calcular_resultado(self):
        pontuacao = {"Futebol": 0, "Padaria": 0, "Sorveteria": 0, "Piscina": 0}
        
        for escolha in self.selecionados:
            for local, caracteristicas in self.dados_locais.items():
                if escolha in caracteristicas:
                    pontuacao[local] += 1
        
        # Encontrar o local com maior pontuação
        resultado = max(pontuacao, key=pontuacao.get)
        
        messagebox.showinfo("Resultado da Detecção", f"O local detectado é: {resultado}")
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DetectorLocal(root)
    root.mainloop()