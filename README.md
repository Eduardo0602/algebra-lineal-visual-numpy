# Álgebra Lineal Visual con NumPy

> Implementación y visualización de conceptos fundamentales de álgebra lineal
> usando Python puro, sin librerías de ML. Priorizando la familiaridad matemática con los conceptos primero, y el código después.

---

## Descripción

Este proyecto visualiza las ideas centrales del álgebra lineal — transformaciones lineales, valores propios, descomposición SVD — como objetos geométricos en el plano. Cada concepto aparece primero como ecuación en LaTeX, luego como implementación en NumPy, y finalmente como gráfico en Matplotlib.

**¿Por qué este proyecto?** Un porcentaje de las personas que aspiran a ser científicos de datos usan el álgebra lineal únicamente como "caja negra". Este proyecto demuestra comprensión real del fundamento matemático y conecta cada concepto con su aplicación concreta en Data Science (PCA, compresión, estabilidad numérica).

El proyecto se estructura en tres notebooks que siguen un arco progresivo: transformaciones → eigenvalores → SVD y PCA.

---

## Contenido Matemático

| Característica | Detalle |
|---|---|
| **Transformaciones visualizadas** | 7 familias: rotación, reflexión (3 tipos), escalado, proyección ortogonal, cizallamiento |
| **Propiedades verificadas numéricamente** | Ortogonalidad, involución, idempotencia, no conmutatividad, grupo de rotaciones |
| **Eigenanálisis** | Polinomio característico, diagonalización, teorema espectral, eigenvalores complejos |
| **SVD** | Factorización completa, interpretación geométrica, teorema de Eckart-Young |
| **Aplicación** | Compresión de imágenes (200×300 y 400×600 px), conexión SVD–PCA |
| **Precisión numérica** | Errores del orden de $10^{-16}$ en todas las verificaciones |

---

## Fundamento Matemático

### Transformaciones lineales

Una aplicación $T: \mathbb{R}^n \to \mathbb{R}^m$ es una **transformación lineal** si y solo si:

$$T(\alpha \mathbf{u} + \beta \mathbf{v}) = \alpha\ T(\mathbf{u}) + \beta\ T(\mathbf{v}) \quad \forall\ \mathbf{u}, \mathbf{v} \in \mathbb{R}^n,\; \forall\ \alpha, \beta \in \mathbb{R}$$

Por el **Teorema de Representación Matricial**, existe una única $A \in \mathbb{R}^{m \times n}$ tal que $T(\mathbf{x}) = A\mathbf{x}$, cuyas columnas son las imágenes de los vectores canónicos: $A = [T(\mathbf{e}_1) \mid \cdots \mid T(\mathbf{e}_n)]$.

El valor absoluto del determinante $|\det(A)|$ mide el **factor de cambio de área** bajo $T$; su signo indica si se preserva ($\det > 0$) o se invierte ($\det < 0$) la orientación.

### Valores y vectores propios

Un vector $\mathbf{v} \neq \mathbf{0}$ es **vector propio** de $A$ con **valor propio** $\lambda$ si:

$$A\mathbf{v} = \lambda \mathbf{v}$$

Los valores propios son las raíces del **polinomio característico** $p(\lambda) = \det(A - \lambda I) = 0$. Propiedades fundamentales: $\sum_i \lambda_i = \text{tr}(A)$ y $\prod_i \lambda_i = \det(A)$

Para matrices **simétricas** ($A = A^T$), el **Teorema Espectral** garantiza: eigenvalores reales, eigenvectors ortogonales, y la descomposición $A = \sum_i \lambda_i \mathbf{v}_i \mathbf{v}_i^T$.

### Descomposición en Valores Singulares (SVD)

Toda matriz $A \in \mathbb{R}^{m \times n}$ admite la factorización:

$$A = U \Sigma V^T$$

La mejor aproximación de rango $k$ a $A$ en norma de Frobenius es la **SVD truncada** (Teorema de Eckart–Young):

$$A_k = \sum_{i=1}^{k} \sigma_i \mathbf{u}_i \mathbf{v}_i^T, \qquad \|A - A_k\|_F = \sqrt{\sigma_{k+1}^2 + \cdots + \sigma_r^2}$$

---

## Resultados Principales

### Notebook 01 — Transformaciones lineales en $\mathbb{R}^2$

- Se implementaron y visualizaron **7 familias de transformaciones**, cada una con su fórmula matricial y su efecto sobre el cuadrado unitario.
- Verificación numérica de propiedades algebraicas con errores del orden de $10^{-16}$: ortogonalidad ($R^T R = I$), involución ($S^2 = I$), idempotencia ($P^2 = P$).
- Demostración visual y cuantitativa de la **no conmutatividad** de la multiplicación matricial: rotar 45° y luego escalar produce un resultado con diferencia máxima de $1.06$ respecto a escalar y luego rotar.

### Notebook 02 — Valores y vectores propios

- Cálculo manual del polinomio característico y verificación contra `np.linalg.eig` (error $= 0$).
- Galería de eigenvectors para 4 tipos de matrices: triangular, simétrica, diagonal y cizallamiento (caso no diagonalizable: multiplicidad geométrica < algebraica).
- La **rotación de 45°** produce eigenvalores complejos $e^{\pm i\pi/4}$, confirmando que ningún vector real mantiene su dirección bajo una rotación pura.
- Visualización de la **convergencia al eigenvector dominante** bajo aplicaciones repetidas de $A$ (principio del Power Method).

### Notebook 03 — SVD y compresión de imágenes

- Demostración de la **interpretación geométrica de la SVD**: toda transformación lineal $2 \times 2$ equivale a rotación → escalado → rotación.
- Imagen sintética ($200 \times 300$ px): con solo $k = 2$ componentes se captura el **98.86% de la energía** con 1.7% del almacenamiento original.
- **Conexión SVD–PCA demostrada algebraicamente y numéricamente**: PC1 explica 81.4% de la varianza. Las varianzas vía SVD y vía eigendescomposición de la covarianza coinciden con error $< 5 \times 10^{-16}$.

---

## Notebooks

| # | Notebook | Descripción |
|---|---|---|
| 01 | [`01_transformaciones_lineales.ipynb`](notebooks/01_transformaciones_lineales.ipynb) | Rotaciones, reflexiones, escalados, proyecciones y cizallamiento en $\mathbb{R}^2$. Composición de transformaciones y no conmutatividad. 13 figuras generadas. |
| 02 | [`02_valores_propios.ipynb`](notebooks/02_valores_propios.ipynb) | Polinomio característico, diagonalización, teorema espectral, eigenvalores complejos. Convergencia al eigenvector dominante. 7 figuras generadas. |
| 03 | [`03_svd_compresion.ipynb`](notebooks/03_svd_compresion.ipynb) | SVD completa, interpretación geométrica, compresión de imágenes, conexión algebraica SVD–PCA. 9 figuras generadas. |

---

## Estructura del Proyecto

```
algebra-lineal-visual-numpy/
├── data/                    # No aplica en este proyecto
├── notebooks/
│   ├── 01_transformaciones_lineales.ipynb
│   ├── 02_valores_propios.ipynb
│   └── 03_svd_compresion.ipynb
├── src/
│   └── visualization.py     # Funciones reutilizables: dibujar_vector, configurar_ejes, comprimir_svd, slugify
├── reports/
│   └── figures/             # 29 visualizaciones exportadas en PNG
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Tecnologías

![Python](https://img.shields.io/badge/Python-3.11-blue)
![NumPy](https://img.shields.io/badge/NumPy-1.x-013243)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-orange)
![SymPy](https://img.shields.io/badge/SymPy-1.x-3B5526)

- **Lenguaje:** Python 3.11
- **Computación matricial:** NumPy
- **Visualización:** Matplotlib
- **Verificación simbólica:** SymPy
- **Entorno:** Conda (`ds_portafolio`) + JupyterLab
- **Control de versiones:** Git + GitHub

---

## Cómo Reproducir

```bash
# 1. Clonar el repositorio
git clone https://github.com/Eduardo0602/algebra-lineal-visual-numpy.git
cd algebra-lineal-visual-numpy

# 2. Crear el entorno con Conda
conda create -n ds_portafolio python=3.11 -y
conda activate ds_portafolio
pip install -r requirements.txt

# 3. Ejecutar los notebooks en orden
jupyter lab
#    Abrir 01 → 02 → 03 y ejecutar Kernel → Restart & Run All en cada uno
```

---

## Lo que Aprendí

1. **El determinante es un objeto geométrico, no un número arbitrario.** Mide exactamente cuánto cambia el área de cualquier región bajo la transformación, y su signo codifica si la orientación se conserva o se invierte.

2. **La multiplicación matricial no es conmutativa, lo cual tiene consecuencias reales.** Rotar 45° y luego escalar no es lo mismo que escalar y luego rotar. Esto importa cada vez que se encadenan transformaciones en Ciencia de Datos (preprocesamiento, PCA, etc.).

3. **Los eigenvectors son las "direcciones invariantes" de una transformación.** El concepto algebraico ($A\mathbf{v} = \lambda\mathbf{v}$) y el geométrico (solo se escala, nunca se desvía) son exactamente la misma cosa.

4. **Una rotación pura no tiene eigenvectors reales.** Eigenvalores complejos no son un problema técnico — son la señal de que ninguna dirección real es invariante. Tiene sentido: una rotación mueve todo.

5. **La no diagonalizabilidad es un fenómeno concreto.** El cizallamiento tiene $\lambda = 1$ con multiplicidad algebraica 2 pero multiplicidad geométrica 1, lo cual implica que no es diagonalizable.

6. **La SVD generaliza la descomposición espectral a cualquier matriz.** No importa si es cuadrada, rectangular, singular o no. Toda matriz admite la factorización $U \Sigma V^T$, convirtiéndose en la herramienta más universal del álgebra lineal.

7. **PCA es SVD aplicada a datos centrados.** Las componentes principales son los vectores singulares derechos de la matriz de datos. Scikit-learn usa SVD internamente porque es numéricamente más estable que calcular $X^T X$ y luego sus eigenvalores.

8. **La aritmética de punto flotante es precisa, pero no exacta.** Errores del orden de $10^{-16}$ son inevitables. La clave es saber cuándo son aceptables y cuándo no.

---

*Proyecto 0.1 del portafolio "De Matemático a Data Scientist" — Fase 0*