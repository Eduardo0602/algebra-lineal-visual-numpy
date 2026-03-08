# CLAUDE.md — Contexto del Proyecto
# Álgebra Lineal Visual con NumPy
# Última actualización: 2026-03-08

---

> Las reglas universales, mi perfil y el comportamiento esperado están en:
> `~/proyectos/CLAUDE.md` (CLAUDE.md global)
> Este archivo contiene SOLO el contexto específico de este proyecto.

---

## 📌 IDENTIFICACIÓN

| Campo | Valor |
|---|---|
| **Nombre del repositorio** | `algebra-lineal-visual-numpy` |
| **Fase del portafolio** | Fase 0 |
| **Proyecto número** | Proyecto 0.1 |
| **Fecha de inicio** | 2026-03-07 |
| **Fecha de cierre real** | 2026-03-08 |
| **Estado** | ✅ COMPLETADO |

---

## 🎯 OBJETIVO DEL PROYECTO

Implementar y visualizar los conceptos fundamentales de álgebra lineal
usando NumPy y Matplotlib. Sin Scikit-learn. Sin librerías de ML.
Solo matemáticas puras expresadas en código.

Este es el primer proyecto del portafolio y el que mejor aprovecha
mi ventaja diferenciadora: demostrar que entiendo la matemática
de verdad antes de usarla como caja negra.

---

## 📊 DATASET

Este proyecto no usa dataset externo — los datos son matrices y vectores
generados programáticamente para visualizar transformaciones lineales.

---

## 🔧 DECISIONES TÉCNICAS

- NumPy para toda la computación matricial (no SciPy para este proyecto)
- Matplotlib para visualizaciones 2D de transformaciones
- SymPy para derivar expresiones en LaTeX y verificar resultados simbólicos
- Jupyter notebooks para combinar LaTeX + código + gráficos

---

## 📈 ESTADO ACTUAL

- **Última sesión:** 2026-03-08
- **Estado:** ✅ COMPLETADO
- **Próximo paso:** Proyecto cerrado — pasar a Proyecto 0.2 EDA con Datos Sucios
- **Bloqueado en:** Nada

---

## 📝 APRENDIZAJES

- Determinante = objeto geométrico (factor de área + orientación)
- Multiplicación matricial no es conmutativa — el orden de transformaciones importa
- Eigenvectors = direcciones invariantes; eigenvalores complejos = sin direcciones invariantes reales
- Cizallamiento: caso canónico de matriz no diagonalizable (mult. geométrica < algebraica)
- SVD generaliza descomposición espectral a toda matriz, sin restricciones
- PCA = SVD sobre datos centrados; Scikit-learn usa SVD por estabilidad numérica ($\kappa(X^TX) = \kappa(X)^2$)
- `NotebookEdit` genera metadata inválida en celdas insertadas — corregir con `nbformat` antes de ejecutar
- `np.linalg.eigh` es preferible a `eig` para matrices simétricas
- Vectorizar loops con `np.cumsum` en lugar de acumular listas

---

## 📁 ESTRUCTURA DE ARCHIVOS RELEVANTE

- Notebooks en: `notebooks/`
- Visualizaciones exportadas en: `reports/figures/`
- Código reutilizable en: `src/`

---

## Contexto global

Ver perfil completo en: `../CLAUDE.md` (directorio padre)

---

*Proyecto cerrado el 2026-03-08. Próximo: Proyecto 0.2 — EDA con Datos Sucios.*