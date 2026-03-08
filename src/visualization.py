"""
visualization.py — Funciones reutilizables de visualización y utilidades.
Proyecto 0.1: Álgebra Lineal Visual con NumPy
"""

import re
import unicodedata

import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------

def slugify(text):
    """
    Converts a string to a safe ASCII filename.

    Removes accented characters, replaces spaces and special symbols with
    underscores, and lowercases the result.

    Parameters
    ----------
    text : str
        Original string (may contain accented chars, spaces, symbols, etc.)

    Returns
    -------
    str
        Lowercase ASCII string suitable for use as a filename.

    Examples
    --------
    >>> slugify("Rotación: θ = 45°")
    'rotacion_theta_45'
    """
    # Descomponer caracteres acentuados (á → a + combining accent)
    text = unicodedata.normalize('NFKD', text)
    # Conservar solo ASCII puro
    text = text.encode('ascii', 'ignore').decode('ascii')
    # Eliminar caracteres que no sean letras, dígitos, espacios o guiones
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    # Colapsar espacios/guiones consecutivos en un solo guion bajo
    text = re.sub(r'[\s_-]+', '_', text)
    return text


# ---------------------------------------------------------------------------
# Visualización de vectores y ejes
# ---------------------------------------------------------------------------

def dibujar_vector(ax, vector, origen=(0, 0), color='blue', label=None, lw=2):
    """
    Draws a vector as an arrow in a 2D plot.

    Parameters
    ----------
    ax     : matplotlib.axes.Axes
        Axes where the vector will be drawn.
    vector : array-like of length 2
        Components (vx, vy) of the vector.
    origen : tuple (x, y), optional
        Starting point of the arrow. Default is (0, 0).
    color  : str, optional
        Arrow color. Default is 'blue'.
    label  : str or None, optional
        Text label placed near the arrow tip.
    lw     : float, optional
        Line width. Default is 2.
    """
    ax.annotate(
        '',
        xy=(origen[0] + vector[0], origen[1] + vector[1]),
        xytext=origen,
        arrowprops=dict(arrowstyle='->', color=color, lw=lw)
    )
    if label:
        # Etiqueta ligeramente más allá de la punta del vector
        ax.text(
            origen[0] + vector[0] * 1.1,
            origen[1] + vector[1] * 1.1,
            label, color=color, fontsize=11, fontweight='bold',
            ha='center', va='center'
        )


def configurar_ejes(ax, titulo, lim=4):
    """
    Configures standard axes for R² visualization.

    Sets symmetric limits, equal aspect ratio, axis lines through the origin,
    title, and axis labels.

    Parameters
    ----------
    ax     : matplotlib.axes.Axes
        Axes to configure.
    titulo : str
        Plot title.
    lim    : float, optional
        Symmetric axis limit [-lim, lim]. Default is 4.
    """
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect('equal')   # Misma escala en ambos ejes — crucial para geometría
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    ax.set_title(titulo, fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')


# ---------------------------------------------------------------------------
# Compresión SVD
# ---------------------------------------------------------------------------

def comprimir_svd(U, sigma, Vt, k):
    """
    Reconstructs a matrix using only the first k singular values (rank-k SVD).

    Computes the rank-k approximation:
        A_k = U[:, :k] @ diag(sigma[:k]) @ Vt[:k, :]

    By the Eckart-Young theorem, this is the best rank-k approximation to A
    in the Frobenius norm.

    Parameters
    ----------
    U     : np.ndarray of shape (m, r)
        Left singular vectors (columns).
    sigma : np.ndarray of shape (r,)
        Singular values in descending order.
    Vt    : np.ndarray of shape (r, n)
        Right singular vectors (rows, already transposed).
    k     : int
        Number of singular components to use. Must satisfy 1 <= k <= r.

    Returns
    -------
    np.ndarray of shape (m, n)
        Rank-k approximation of the original matrix.
    """
    return U[:, :k] @ np.diag(sigma[:k]) @ Vt[:k, :]
