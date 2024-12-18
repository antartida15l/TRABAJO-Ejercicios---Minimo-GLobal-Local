import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Título de la aplicación
st.title("Resolviendo problemas de optimización con Streamlit")
st.markdown("""
Esta aplicación interactiva te ayudará a visualizar y entender los conceptos de mínimos globales y locales 
en varias funciones matemáticas. A continuación, selecciona el ejercicio que deseas explorar:
""")

# Sidebar para seleccionar ejercicios
exercise = st.sidebar.selectbox(
    "Selecciona un ejercicio",
    ("Ejercicio 1: Minimización de $f(x) = x^2 - 4x + 5$",
     "Ejercicio 2: Análisis de $f(x) = |x|$",
     "Ejercicio 3: $f(x) = \\sin(x)$ en $[0, \\pi]$",
     "Ejercicio 4: $f(x, y) = x^2 + y^2$ con $x^2 + y^2 \\leq 1$",
     "Ejercicio 5: Ejemplo con mínimo global no único")
)

# Ejercicio 1
if exercise == "Ejercicio 1: Minimización de $f(x) = x^2 - 4x + 5$":
    st.subheader("Minimización de $f(x) = x^2 - 4x + 5$")
    st.markdown("""
    La función cuadrática $f(x) = x^2 - 4x + 5$ tiene un mínimo global en $x = 2$, como se demuestra al reescribir 
    la función en forma estándar: $f(x) = (x - 2)^2 + 1$. A continuación, puedes ver la gráfica.
    """)

    # Definir la función
    def f1(x):
        return x**2 - 4*x + 5

    # Generar los valores
    x_vals = np.linspace(-2, 6, 500)
    y_vals = f1(x_vals)

    # Crear el gráfico
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label='$f(x) = x^2 - 4x + 5$', color='blue')
    ax.scatter([2], [f1(2)], color='red', label='Mínimo global en $x=2$')
    ax.scatter([0], [f1(0)], color='green', label='$x=0$ no es mínimo')
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
    ax.axvline(2, color='red', linestyle='--')
    ax.legend()
    ax.grid()
    ax.set_title("Gráfica de $f(x)$")
    st.pyplot(fig)

# Ejercicio 2
elif exercise == "Ejercicio 2: Análisis de $f(x) = |x|$":
    st.subheader("Análisis de $f(x) = |x|$")
    st.markdown("""
    La función $f(x) = |x|$ tiene un mínimo global y local en $x = 0$, ya que $f(0) = 0$ es el menor valor posible 
    en todo el dominio de la función.
    """)

    # Definir la función
    def f2(x):
        return np.abs(x)

    # Generar los valores
    x_vals = np.linspace(-2, 2, 500)
    y_vals = f2(x_vals)

    # Crear el gráfico
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label='$f(x) = |x|$', color='orange')
    ax.scatter([0], [f2(0)], color='red', label='Mínimo global en $x=0$')
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
    ax.axvline(0, color='red', linestyle='--')
    ax.legend()
    ax.grid()
    ax.set_title("Gráfica de $f(x) = |x|$")
    st.pyplot(fig)

# Ejercicio 3
elif exercise == "Ejercicio 3: $f(x) = \\sin(x)$ en $[0, \\pi]$":
    st.subheader("Análisis de $f(x) = \\sin(x)$ en $[0, \\pi]$")
    st.markdown("""
    En el intervalo $[0, \\pi]$, la función $\\sin(x)$ alcanza su mínimo global en $x = \\pi$, con un valor de $f(\\pi) = 0$.
    """)

    # Definir la función
    def f3(x):
        return np.sin(x)

    # Generar los valores
    x_vals = np.linspace(0, np.pi, 500)
    y_vals = f3(x_vals)

    # Crear el gráfico
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label='$f(x) = \\sin(x)$', color='purple')
    ax.scatter([np.pi], [f3(np.pi)], color='red', label='Mínimo global en $x=\\pi$')
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
    ax.axvline(np.pi, color='red', linestyle='--')
    ax.legend()
    ax.grid()
    ax.set_title("Gráfica de $f(x) = \\sin(x)$")
    st.pyplot(fig)

# Ejercicio 4
elif exercise == "Ejercicio 4: $f(x, y) = x^2 + y^2$ con $x^2 + y^2 \\leq 1$":
    st.subheader("Análisis de $f(x, y) = x^2 + y^2$")
    st.markdown("""
    La función $f(x, y) = x^2 + y^2$ alcanza su mínimo global en el origen $(0, 0)$, donde $f(0, 0) = 0$.
    """)

    # Definir la función
    def f4(x, y):
        return x**2 + y**2

    # Crear el gráfico
    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = f4(X, Y)

    fig, ax = plt.subplots()
    c = ax.contourf(X, Y, Z, levels=50, cmap='viridis')
    fig.colorbar(c, ax=ax)
    ax.set_title("Gráfica de $f(x, y) = x^2 + y^2$")
    st.pyplot(fig)

# Ejercicio 5
elif exercise == "Ejercicio 5: Ejemplo con mínimo global no único":
    st.subheader("Ejemplo con mínimo global no único")
    st.markdown("""
    La función $f(x) = \\max(|x - 1|, |x + 1|)$ tiene mínimos globales no únicos para $x \\in [-1, 1]$, ya que 
    $f(x) = 1$ en ese intervalo.
    """)

    # Definir la función
    def f5(x):
        return np.maximum(np.abs(x - 1), np.abs(x + 1))

    # Generar los valores
    x_vals = np.linspace(-3, 3, 500)
    y_vals = f5(x_vals)

    # Crear el gráfico
    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label='$f(x) = \\max(|x-1|, |x+1|)$', color='green')
    ax.axhline(1, color='red', linestyle='--', label='Mínimo global en $x \\in [-1, 1]$')
    ax.fill_between(x_vals, y_vals, where=(x_vals >= -1) & (x_vals <= 1), color='green', alpha=0.3)
    ax.legend()
    ax.grid()
    ax.set_title("Gráfica de $f(x)$")
    st.pyplot(fig)
