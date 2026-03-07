# Álgebra Lineal Visual con NumPy

> Implementación y visualización de conceptos fundamentales de álgebra lineal
> usando Python puro — sin librerías de ML. La matemática primero, el código después.

---

## Descripción

Este proyecto visualiza las ideas centrales del álgebra lineal
— transformaciones lineales, valores propios, descomposición SVD —
como objetos geométricos en el plano. Cada concepto aparece primero
como ecuación en LaTeX, luego como implementación en NumPy,
y finalmente como gráfico en Matplotlib.

**¿Por qué este proyecto?** El 99% de los científicos de datos usan
álgebra lineal como caja negra. Este notebook demuestra comprensión
real del fundamento matemático.

---

## Fundamento Matemático

*(Esta sección es la firma del portafolio)*

### Transformaciones lineales

Una transformación lineal $T: \mathbb{R}^n \to \mathbb{R}^m$ preserva
la suma de vectores y la multiplicación por escalar:
$$T(\alpha \mathbf{u} + \beta \mathbf{v}) = \alpha T(\mathbf{u}) + \beta T(\mathbf{v})$$

Toda transformación lineal en dimensión finita se representa como
multiplicación matricial: $T(\mathbf{x}) = A\mathbf{x}$.

### Valores y vectores propios

Un vector $\mathbf{v} \neq \mathbf{0}$ es vector propio de $A$
con valor propio $\lambda$ si:
$$A\mathbf{v} = \lambda \mathbf{v}$$

Geométricamente: la transformación solo escala $\mathbf{v}$,
sin cambiar su dirección.

### Descomposición en Valores Singulares (SVD)

Toda matriz $A \in \mathbb{R}^{m \times n}$ admite la factorización:
$$A = U \Sigma V^T$$

donde $U$ y $V$ son ortogonales y $\Sigma$ es diagonal con los
valores singulares $\sigma_1 \geq \sigma_2 \geq \cdots \geq 0$.

---

## Tecnologías

- Python 3.11
- NumPy — computación matricial
- Matplotlib — visualización
- SymPy — verificación simbólica y generación de LaTeX
- Jupyter Notebook — documentación integrada

---

## Estructura del proyecto
```
algebra-lineal-visual-numpy/
├── data/                    # No aplica en este proyecto
├── notebooks/
│   ├── 01_transformaciones_lineales.ipynb
│   ├── 02_valores_propios.ipynb
│   └── 03_svd_compresion.ipynb
├── src/                     # Funciones reutilizables
├── reports/figures/         # Gráficos exportados
├── CLAUDE.md
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Cómo reproducir
```bash
# Clonar el repositorio
git clone https://github.com/TU-USUARIO/algebra-lineal-visual-numpy.git
cd algebra-lineal-visual-numpy

# Crear entorno conda
conda create -n algebra-lineal python=3.11
conda activate algebra-lineal
pip install -r requirements.txt

# Ejecutar los notebooks
jupyter notebook notebooks/
```

---

## Resultados principales

*(Se actualizará con las visualizaciones al completar los notebooks)*

---

## Lo que aprendí

*(Se actualizará al completar el proyecto)*

---

*Proyecto 0.1 del portafolio "De Matemático a Data Scientist" — Fase 0*
```

Guarda con `Ctrl+S`.

---

### Archivo 4 — `requirements.txt`

📁 Haz clic en `requirements.txt` y pega:
```
numpy
matplotlib
sympy
jupyter