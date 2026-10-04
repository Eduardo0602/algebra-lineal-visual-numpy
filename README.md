<p align="right"><b>English</b> · <a href="README.es.md">Español</a></p>

# Visual linear algebra with NumPy: what a matrix does, geometrically

Linear maps, eigenvalues and SVD implemented from NumPy and visualized in the plane: first the equation, then the code, then the plot.

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C) ![License](https://img.shields.io/badge/license-MIT-green) [![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Eduardo0602/algebra-lineal-visual-numpy/blob/main/notebooks/01_transformaciones_lineales.ipynb)

## The problem

Many people training in data science use linear algebra as a black box: they call `PCA()` or `np.linalg.svd` without knowing what it does. This project shows each concept as a geometric object, implements it from NumPy primitives and connects it to its use in data science (PCA, compression, numerical stability). The arc is progressive: transformations, eigenvalues, SVD and PCA.

## Contents

| Topic | Detail |
|---|---|
| Visualized transformations | 7 families: rotation, reflection (3 types), scaling, orthogonal projection, shear |
| Numerically verified properties | Orthogonality, involution, idempotence, non-commutativity, rotation group |
| Eigenvalues | Characteristic polynomial, diagonalization, spectral theorem, complex eigenvalues |
| SVD | Full factorization, geometric interpretation, Eckart–Young theorem |
| Application | Compression of synthetic images (200×300 and 400×600 px), SVD–PCA connection |

## Mathematical foundation

**Linear maps.** $`T: \mathbb{R}^n \to \mathbb{R}^m`$ is linear if $`T(\alpha \mathbf{u} + \beta \mathbf{v}) = \alpha\, T(\mathbf{u}) + \beta\, T(\mathbf{v})`$ for all $`\mathbf{u}, \mathbf{v} \in \mathbb{R}^n`$ and $`\alpha, \beta \in \mathbb{R}`$. By the matrix representation theorem there is a unique $`A \in \mathbb{R}^{m \times n}`$ with $`T(\mathbf{x}) = A\mathbf{x}`$, whose columns are the images of the standard basis vectors: $`A = [T(\mathbf{e}_1) \mid \cdots \mid T(\mathbf{e}_n)]`$. The absolute value of $`\det(A)`$ is the area scaling factor and its sign tells whether orientation is preserved.

**Eigenvalues and eigenvectors.** $`\mathbf{v} \neq \mathbf{0}`$ is an eigenvector of $`A`$ with eigenvalue $`\lambda`$ if $`A\mathbf{v} = \lambda \mathbf{v}`$. The eigenvalues are the roots of $`p(\lambda) = \det(A - \lambda I)`$, with $`\sum_i \lambda_i = \text{tr}(A)`$ and $`\prod_i \lambda_i = \det(A)`$. If $`A = A^\top`$, the spectral theorem guarantees real eigenvalues, orthogonal eigenvectors and $`A = \sum_i \lambda_i \mathbf{v}_i \mathbf{v}_i^\top`$.

**Singular value decomposition.** Every $`A \in \mathbb{R}^{m \times n}`$ admits $`A = U \Sigma V^\top`$. The best rank-$`k`$ approximation in Frobenius norm is the truncated SVD (Eckart–Young theorem):

```math
A_k = \sum_{i=1}^{k} \sigma_i \mathbf{u}_i \mathbf{v}_i^\top, \qquad \|A - A_k\|_F = \sqrt{\sigma_{k+1}^2 + \cdots + \sigma_r^2}.
```

## Results

**Transformations in $`\mathbb{R}^2`$.** 7 families were implemented, each with its matrix and its effect on the unit square. The algebraic properties were verified with errors of order $`10^{-16}`$: orthogonality ($`R^\top R = I`$), involution ($`S^2 = I`$) and idempotence ($`P^2 = P`$). Rotating 45° and then scaling differs from scaling and then rotating by up to $`1.06`$: non-commutativity is visible and measurable.

**Eigenvalues.** The characteristic polynomial computed by hand matches `np.linalg.eig` (error $`= 0`$). The shear illustrates a non-diagonalizable case (geometric multiplicity smaller than algebraic) and the 45° rotation produces complex eigenvalues $`e^{\pm i\pi/4}`$: no real vector keeps its direction. Applying $`A`$ repeatedly converges to the dominant eigenvector (the principle of the power method).

**SVD and compression.** Every $`2 \times 2`$ transformation is a rotation, a scaling and a rotation. In the synthetic $`200 \times 300`$ px image, $`k = 2`$ components capture **98.86 % of the energy** with 1.7 % of the storage. PCA and SVD agree algebraically and numerically: the first component explains 81.4 % of the variance and the variances computed both ways differ by less than $`5 \times 10^{-16}`$.

![SVD compression](reports/figures/svd_compresion_comparativa.png)

## Verification

Every stated property is checked numerically in the notebooks (orthogonality, involution, idempotence, characteristic polynomial versus `np.linalg.eig`, PCA variances by SVD versus the covariance matrix), with errors of order $`10^{-16}`$ or smaller (exactly $`0`$ for the characteristic polynomial).

## How to reproduce

```bash
git clone https://github.com/Eduardo0602/algebra-lineal-visual-numpy.git
cd algebra-lineal-visual-numpy
conda create -n ds_portafolio python=3.11 -y
conda activate ds_portafolio
pip install -r requirements.txt
jupyter lab   # open 01, 02 and 03 in order: Kernel → Restart & Run All
```

| Notebook | Contents |
|---|---|
| [`01_transformaciones_lineales.ipynb`](notebooks/01_transformaciones_lineales.ipynb) | Rotations, reflections, scalings, projections and shear; composition and non-commutativity (13 figures) |
| [`02_valores_propios.ipynb`](notebooks/02_valores_propios.ipynb) | Characteristic polynomial, diagonalization, spectral theorem, complex eigenvalues, convergence to the dominant eigenvector (7 figures) |
| [`03_svd_compresion.ipynb`](notebooks/03_svd_compresion.ipynb) | SVD, geometric interpretation, image compression, SVD–PCA connection (9 figures) |

Notebooks and code comments are in Spanish.

## Project structure

```
algebra-lineal-visual-numpy/
├── notebooks/            # 01 → 02 → 03
├── src/visualization.py  # dibujar_vector, configurar_ejes, comprimir_svd, slugify
├── reports/figures/      # 29 PNG figures
├── requirements.txt
└── LICENSE
```

## Limitations

- Everything happens in $`\mathbb{R}^2`$ and with synthetic images: the goal is geometric intuition, not performance on large data.
- SVD compression is compared by energy and Frobenius error, not by perceptual quality.

## What I learned

1. **The determinant is a geometric object.** It measures how much area changes under the transformation, and its sign encodes orientation.
2. **Matrix multiplication is not commutative, and that matters.** Chaining transformations in another order (preprocessing, PCA) changes the result.
3. **Eigenvectors are the invariant directions.** The algebraic and the geometric definitions are the same thing.
4. **A pure rotation has no real eigenvectors.** Complex eigenvalues are not a technical problem: they signal that no real direction is preserved.
5. **Non-diagonalizability is concrete.** The shear has $`\lambda = 1`$ with algebraic multiplicity 2 and geometric multiplicity 1.
6. **SVD generalizes the spectral decomposition to any matrix**, square or not, singular or not.
7. **PCA is the SVD of centered data.** That is why scikit-learn uses SVD: it is more stable than diagonalizing $`X^\top X`$.
8. **Floating point is precise but not exact.** Errors of $`10^{-16}`$ are unavoidable; the craft is knowing when they matter.

---

### Portfolio *From Mathematician to Data Scientist*

| Project | Question | Tools |
|---|---|---|
| [Complex survey sampling with Ser Estudiante](https://github.com/Eduardo0602/muestreo-complejo-ser-estudiante) | How wrong is an analysis that ignores the sampling design? | R, survey |
| [Messy-data EDA: deaths 2021](https://github.com/Eduardo0602/eda-limpieza-defunciones-ecuador-pandas-sql) | What must be fixed before trusting an official registry? | Python, pandas, SQL |
| [Linear regression from scratch](https://github.com/Eduardo0602/regresion-lineal-numpy-desde-cero) | Can a plane predict how deep Ecuador's earthquakes are? | Python, NumPy |
| **Visual linear algebra** (this repository) | What does a matrix do, geometrically? | Python, NumPy |

Eduardo Araque · Mathematician (Universidad Central del Ecuador) · [GitHub](https://github.com/Eduardo0602) · [LinkedIn](https://www.linkedin.com/in/eduardo-araque-jacome-math)
