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

Una función $T: \mathbb{R}^n \to \mathbb{R}^m$ es una **transformación lineal** si y solo si:

$$T(\alpha \mathbf{u} + \beta \mathbf{v}) = \alpha\, T(\mathbf{u}) + \beta\, T(\mathbf{v}) \quad \forall\, \mathbf{u}, \mathbf{v} \in \mathbb{R}^n,\; \forall\, \alpha, \beta \in \mathbb{R}$$

Por el **Teorema de Representación Matricial**, existe una única $A \in \mathbb{R}^{m \times n}$ tal que
$T(\mathbf{x}) = A\mathbf{x}$, cuyas columnas son las imágenes de los vectores canónicos:
$A = [T(\mathbf{e}_1) \mid \cdots \mid T(\mathbf{e}_n)]$.

El valor absoluto del determinante $|\det(A)|$ mide el **factor de cambio de área** bajo $T$;
su signo indica si se preserva ($\det > 0$) o se invierte ($\det < 0$) la orientación.

### Valores y vectores propios

Un vector $\mathbf{v} \neq \mathbf{0}$ es **vector propio** de $A$ con **valor propio** $\lambda$ si:

$$A\mathbf{v} = \lambda \mathbf{v}$$

Los valores propios son las raíces del **polinomio característico**
$p(\lambda) = \det(A - \lambda I) = 0$.
Para matrices $2 \times 2$: $p(\lambda) = \lambda^2 - \operatorname{tr}(A)\lambda + \det(A)$.

Propiedades fundamentales:

$$\sum_i \lambda_i = \operatorname{tr}(A), \qquad \prod_i \lambda_i = \det(A)$$

Si $A$ es **diagonalizable**, existe la factorización $A = PDP^{-1}$, que reduce
el cálculo de $A^k$ a elevar escalares: $A^k = P D^k P^{-1}$.

Para matrices **simétricas** ($A = A^T$), el **Teorema Espectral** garantiza:
eigenvalores reales, eigenvectors ortogonales, y la descomposición
$A = \sum_i \lambda_i \mathbf{v}_i \mathbf{v}_i^T$.

### Descomposición en Valores Singulares (SVD)

Toda matriz $A \in \mathbb{R}^{m \times n}$ admite la factorización:

$$A = U \Sigma V^T$$

donde $U \in \mathbb{R}^{m \times m}$ y $V \in \mathbb{R}^{n \times n}$ son ortogonales, y
$\Sigma$ es diagonal con $\sigma_1 \geq \sigma_2 \geq \cdots \geq \sigma_r > 0$.

Los valores singulares satisfacen $\sigma_i = \sqrt{\lambda_i(A^T A)}$, conectando
directamente SVD con la descomposición espectral.

La mejor aproximación de rango $k$ a $A$ en norma de Frobenius es la
**SVD truncada** (Teorema de Eckart–Young):

$$A_k = \sum_{i=1}^{k} \sigma_i \mathbf{u}_i \mathbf{v}_i^T, \qquad \|A - A_k\|_F = \sqrt{\sigma_{k+1}^2 + \cdots + \sigma_r^2}$$

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
├── reports/figures/         # Gráficos exportados (29 PNG)
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

# Activar entorno conda
conda activate ds_portafolio

# Ejecutar los notebooks en orden
jupyter notebook notebooks/
```

---

## Resultados principales

### Notebook 01 — Transformaciones lineales en $\mathbb{R}^2$

- Se implementaron y visualizaron **7 familias de transformaciones**: rotación, reflexión sobre
  eje $x$, reflexión sobre eje $y$, reflexión sobre $y = x$, escalado, proyección ortogonal y
  cizallamiento, cada una con su fórmula matricial y su efecto sobre el cuadrado unitario.
- Verificación numérica de propiedades algebraicas con errores del orden de $10^{-16}$:
  ortogonalidad ($R^T R = I$), involución ($S^2 = I$), idempotencia ($P^2 = P$).
- Demostración visual y cuantitativa de la **no conmutatividad** de la multiplicación matricial:
  rotar 45° y luego escalar produce un resultado con diferencia máxima de $1.06$ respecto a
  escalar y luego rotar.
- Tabla comparativa del determinante: todas las transformaciones que preservan área tienen
  $|\det| = 1$; la proyección tiene $\det = 0$ (colapso de dimensión).

### Notebook 02 — Valores y vectores propios

- Cálculo manual del polinomio característico y verificación contra `np.linalg.eig`
  (error $= 0$ para la matriz triangular del ejemplo).
- Galería de eigenvectors para 4 tipos de matrices: triangular, simétrica, diagonal
  y cizallamiento. Este último ilustra el único caso con $\lambda = 1$ de multiplicidad
  algebraica 2 pero multiplicidad geométrica 1 (no diagonalizable).
- La **rotación de 45°** produce eigenvalores complejos $e^{\pm i\pi/4}$, confirmando que
  ningún vector real mantiene su dirección bajo una rotación pura.
- Verificación de la **descomposición espectral** $A = \sum_i \lambda_i \mathbf{v}_i \mathbf{v}_i^T$
  con error $6.66 \times 10^{-16}$.
- Visualización de la **convergencia al eigenvector dominante** bajo aplicaciones
  repetidas de $A$ (principio del Power Method).
- Potencias de matrices vía diagonalización: $A^{10}$ calculado con error $< 6 \times 10^{-11}$
  respecto al resultado directo.

### Notebook 03 — SVD y compresión de imágenes

- Demostración de la **interpretación geométrica de la SVD**: toda transformación lineal
  $2 \times 2$ equivale a rotación → escalado (elipse) → rotación.
- Imagen sintética ($200 \times 300$ px): con solo $k = 2$ componentes se captura el
  **98.86% de la energía** con 1.7% del almacenamiento original. Con $k = 5$: 99.78% de
  energía, 4.2% del almacenamiento.
- Visualización capa por capa: las primeras capas capturan estructura global, las últimas
  son esencialmente ruido.
- **Conexión SVD–PCA demostrada algebraicamente y numéricamente**: en datos 2D
  correlacionados, PC1 explica 81.4% de la varianza. Las varianzas vía SVD y vía
  eigendescomposición de la covarianza coinciden con error $< 5 \times 10^{-16}$.
- Curva error vs. compresión para imagen compleja ($400 \times 600$ px): identifica el
  punto de rendimiento decreciente en la relación calidad/almacenamiento.

---

## Lo que aprendí

1. **El determinante es un objeto geométrico, no un número arbitrario.** Mide exactamente
   cuánto cambia el área de cualquier región bajo la transformación, y su signo codifica
   si la orientación se conserva o se invierte.

2. **La multiplicación matricial no es conmutativa — y eso tiene consecuencias reales.**
   Rotar 45° y luego escalar no es lo mismo que escalar y luego rotar. Esto importa cada
   vez que se encadenan transformaciones en Data Science (preprocesamiento, PCA, etc.).

3. **Los eigenvectors son las "direcciones invariantes" de una transformación.** El concepto
   algebraico ($A\mathbf{v} = \lambda\mathbf{v}$) y el geométrico (solo se escala, nunca se
   desvía) son exactamente la misma cosa. Visualizarlo lo hace irrefutable.

4. **Una rotación pura no tiene eigenvectors reales.** Eigenvalores complejos no son
   un problema técnico, son la señal de que ninguna dirección real es invariante.
   Tiene sentido: una rotación mueve todo.

5. **La no diagonalizabilidad es un fenómeno concreto.** El cizallamiento tiene
   $\lambda = 1$ con multiplicidad algebraica 2 pero multiplicidad geométrica 1.
   No es diagonalizable. Esto no es solo teoría: NumPy produce los valores correctos pero
   el resultado no se puede usar como si la matriz fuera diagonal.

6. **La SVD generaliza la descomposición espectral a cualquier matriz.** No importa si es
   cuadrada, rectangular, singular o no. Toda matriz admite la factorización $U \Sigma V^T$.
   Es la herramienta más universal del álgebra lineal.

7. **PCA es SVD aplicada a datos centrados — no es una caja negra.** Las componentes
   principales son los vectores singulares derechos de la matriz de datos. Scikit-learn
   usa SVD internamente porque es numéricamente más estable que calcular $X^T X$ y luego
   sus eigenvalores.

8. **La aritmética de punto flotante es precisa pero no exacta.** Errores del orden de
   $10^{-16}$ son inevitables. La clave es saber cuándo son aceptables y cuándo no.

---

*Proyecto 0.1 del portafolio "De Matemático a Data Scientist" — Fase 0*
