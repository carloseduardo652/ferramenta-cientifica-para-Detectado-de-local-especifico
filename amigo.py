import tkinter as tk
from tkinter import messagebox
import random

MAX_ESCOLHAS = 10

# ===================== BASE DE CONHECIMENTO =====================

base_conhecimento = {
    "Futebol": [
        "Movimento — 10–13 km/jogo",
        "Deslocamento — ≈ 50 m",
        "Trajetória — 40–60 m",
        "Velocidade — até 36 km/h",
        "Aceleração — ≈ 4 m/s²",
        "Movimento parabólico — 30°–45°",
        "Inércia — 65–90 kg",
        "Força aplicada — ≈ 1000 N",
        "Ação e reação — ≈ 1000 N",
        "Força gravitacional — 700–900 N",
        "Força normal — 700–900 N",
        "Força elástica — deformação em ms",
        "Impulso — 10–20 N•s",
        "Atrito — 0,6–0,8",
        "Energia cinética — 100–150 J",
        "Energia potencial gravitacional — 20–50 J",
        "Transformação de energia — 800–1200 kcal",
        "Movimento rotacional — 50–100 rad/s",
        "Propagação do som no ar — 343 m/s",
        "Intensidade sonora — 100–120 dB",
        "Trocas térmicas por evaporação — 1–3 L",
        "Produção de calor metabólico — 800–1200 kcal",
        "Arrasto do ar — 0,1–1 N",
        "Turbulência do ar — ≈ 10⁵",
        "Respiração celular — 60–75 mL/kg/min",
        "Equilíbrio ácido–base — pH 7,4",
        "Liberação de neurotransmissores — ↑ nmol/L"
    ],
    "Padaria": [
        "Temperatura — 180–250 °C",
        "Calor — 2–4 MJ",
        "Transferência de calor — 5–10 kW",
        "Condução térmica — 0,5–1,5 W/m•K",
        "Convecção — 1–3 m/s",
        "Radiação térmica — 5–20 kW/m²",
        "Dilatação térmica — 1–3 mm",
        "Pressão — 1 atm",
        "Força — 50–150 N",
        "Trabalho — 100–300 J",
        "Energia — 3–6 MJ",
        "Potência — 5–20 kW",
        "Atrito — 0,3–0,6",
        "Gravidade — 9,8 m/s²",
        "Massa — 0,5–1 kg",
        "Densidade — 0,2–0,4 g/cm³",
        "Volume — 1–2 L",
        "Viscosidade — 10³–10⁴ Pa•s",
        "Umidade — 60–80 %",
        "Mudança de estado físico — 100 °C",
        "Carbono — 45–50 %",
        "Hidrogênio — 6–7 %",
        "Oxigênio — 40–45 %",
        "Nitrogênio — 2–3 %",
        "Sódio — 1–2 %",
        "Cloro — 1–2 %",
        "Cálcio — 20–50 mg/100 g",
        "Ferro — 2–4 mg/100 g"
    ],
    "Sorveteria": [
        "Temperatura — −20 a −5 °C",
        "Calor — 1–3 MJ",
        "Transferência de calor — 2–8 kW",
        "Condução térmica — 0,4–1,0 W/m•K",
        "Convecção — 0,5–2 m/s",
        "Radiação térmica — 2–10 kW/m²",
        "Mudança de estado físico — 0 °C",
        "Solidificação — −5 a −10 °C",
        "Fusão — −2 a 0 °C",
        "Pressão — 1–2 atm",
        "Energia — 2–5 MJ",
        "Trabalho — 50–200 J",
        "Potência — 1–5 kW",
        "Atrito — 0,2–0,4",
        "Gravidade — 9,8 m/s²",
        "Massa — 0,1–1 kg",
        "Densidade — 0,5–0,7 g/cm³",
        "Volume — 0,1–1 L",
        "Viscosidade — 10²–10³ Pa•s",
        "Refrigeração — −20 °C",
        "Carbono — 40–50 %",
        "Hidrogênio — 6–8 %",
        "Oxigênio — 40–45 %",
        "Nitrogênio — 1–2 %",
        "Sódio — 30–80 mg/100 g",
        "Cálcio — 100–150 mg/100 g",
        "Potássio — 150–250 mg/100 g",
        "Fósforo — 80–120 mg/100 g",
        "Enxofre — 0,1–0,3 %",
        "Magnésio — 10–30 mg/100 g"
    ],
    "Piscina": [
        "Flutuação — 0,98–1,02 g/cm³",
        "Empuxo — 600–800 N",
        "Densidade — 1,0 g/cm³",
        "Pressão hidrostática — 1,2 atm",
        "Volume — 50–500 m³",
        "Massa — 1000 kg/m³",
        "Gravidade — 9,8 m/s²",
        "Força — 200–600 N",
        "Aceleração — 1–3 m/s²",
        "Velocidade — 1–2 m/s",
        "Resistência do fluido — 10–100 N",
        "Atrito — 0,02–0,05",
        "Tensão superficial — 0,072 N/m",
        "Capilaridade — 1–5 mm",
        "Temperatura — 26–30 °C",
        "Calor — 10–50 MJ",
        "Transferência de calor — 5–20 kW",
        "Dilatação térmica — 0,2 %",
        "Ondas — 0,5–2 Hz",
        "Refração — 1,33",
        "Hidrogênio — 11 %",
        "Oxigênio — 89 %",
        "Cloro — 1–3 ppm",
        "Sódio — 10–50 mg/L",
        "Cálcio — 200–400 ppm",
        "Carbono — 1–5 ppm",
        "Nitrogênio — < 1 ppm",
        "Magnésio — 10–50 ppm"
    ]
}

# ===================== PREPARAÇÃO =====================

todas_opcoes = []
mapa_opcao_local = {}

for local, lista in base_conhecimento.items():
    for item in lista:
        todas_opcoes.append(item)
        mapa_opcao_local[item] = local

random.shuffle(todas_opcoes)

# ===================== INTERFACE =====================

root = tk.Tk()
root.title("Ferramenta Científica para Detecção de Local")
root.geometry("950x600")

selecionadas = {}
contador = tk.IntVar(value=0)

tk.Label(
    root,
    text="Você deve escolher o mais importante ao local específico que deseja encontrar",
    font=("Arial", 12, "bold")
).pack(pady=10)

lbl_contador = tk.Label(root, text="Escolhas restantes: 10", font=("Arial", 11))
lbl_contador.pack()

canvas = tk.Canvas(root)
scroll = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
frame = tk.Frame(canvas)

frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame, anchor="nw")
canvas.configure(yscrollcommand=scroll.set)

canvas.pack(side="left", fill="both", expand=True)
scroll.pack(side="right", fill="y")

def atualizar_contador():
    lbl_contador.config(text=f"Escolhas restantes: {MAX_ESCOLHAS - contador.get()}")

def selecionar(item, var):
    if var.get():
        if contador.get() >= MAX_ESCOLHAS:
            var.set(False)
            messagebox.showwarning("Limite", "Máximo de 10 escolhas permitidas.")
            return
        selecionadas[item] = mapa_opcao_local[item]
        contador.set(contador.get() + 1)
    else:
        if item in selecionadas:
            del selecionadas[item]
            contador.set(contador.get() - 1)
    atualizar_contador()

def detectar():
    if contador.get() == 0:
        messagebox.showinfo("Resultado", "Nenhuma opção selecionada.")
        return

    contagem = {}
    for local in base_conhecimento:
        contagem[local] = 0

    for local in selecionadas.values():
        contagem[local] += 1

    resultado = max(contagem, key=contagem.get)

    messagebox.showinfo("Local Detectado", f"Local mais provável:\n\n👉 {resultado}")

for opcao in todas_opcoes:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(
        frame,
        text=opcao,
        variable=var,
        command=lambda o=opcao, v=var: selecionar(o, v),
        wraplength=850,
        justify="left"
    )
    chk.pack(anchor="w")

tk.Button(
    root,
    text="Detectar Local",
    font=("Arial", 12, "bold"),
    bg="lightblue",
    command=detectar
).pack(pady=10)

root.mainloop()
