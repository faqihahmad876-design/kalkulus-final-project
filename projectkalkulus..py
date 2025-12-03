# Tugascalkulus.py
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, diff, lambdify, SympifyError
from sympy import sin, cos, tan, exp, log

# ============================
#   CONFIG
# ============================
st.set_page_config(page_title="Kalkulus - Plot & Turunan", layout="centered")

st.title("📘 Aplikasi Kalkulus: Plot Fungsi & Turunan")
st.write("Masukkan fungsi matematika satu variabel `x`.\n"
         "Gunakan `**` untuk pangkat (contoh: `x**2 + 3*x - 1`, `sin(x)`, `exp(-x)`)")


# ============================
#   INPUT USER
# ============================
func_input = st.text_input("Masukkan fungsi f(x):", value="sin(x)")

col1, col2 = st.columns(2)
with col1:
    x_min = st.number_input("x minimum", value=-10.0)
with col2:
    x_max = st.number_input("x maksimum", value=10.0)

samples = st.slider("Jumlah titik sampel", 100, 3000, 800)
show_grid = st.checkbox("Tampilkan grid", True)

plot_style = st.selectbox(
    "Gaya plot",
    ["Line", "Scatter", "Line + Scatter"]
)

st.write("---")

# ============================
#   PROSES KALKULUS
# ============================
x = symbols("x")

try:
    # Parse fungsi
    f_sym = sympify(func_input)
    f_prime_sym = diff(f_sym, x)

    st.subheader("Turunan Simbolik f'(x)")
    st.latex(f"f'(x) = {f_prime_sym}")

    # Ubah ke fungsi numerik
    f_num = lambdify(x, f_sym, "numpy")
    f_prime_num = lambdify(x, f_prime_sym, "numpy")

    xs = np.linspace(x_min, x_max, samples)

    # Evaluasi aman
    def safe_eval(fn, arr):
        try:
            vals = fn(arr)
            vals = np.array(vals, dtype=float)
            vals = np.where(np.isfinite(vals), vals, np.nan)
            return vals
        except:
            return np.full_like(arr, np.nan, dtype=float)

    ys = safe_eval(f_num, xs)
    yps = safe_eval(f_prime_num, xs)

    # Fallback turunan numerik
    if np.all(np.isnan(yps)):
        try:
            yps = np.gradient(ys, xs)
            st.info("Menggunakan turunan numerik (fallback).")
        except:
            st.error("Gagal menghitung turunan. Periksa fungsi dan domain.")
            st.stop()

    # ============================
    #   PLOT F(X)
    # ============================
    st.subheader("Plot f(x)")
    fig1, ax1 = plt.subplots(figsize=(7, 4))

    if plot_style == "Line":
        ax1.plot(xs, ys)
    elif plot_style == "Scatter":
        ax1.scatter(xs, ys, s=10)
    else:
        ax1.plot(xs, ys)
        ax1.scatter(xs, ys, s=10)

    ax1.set_title("f(x)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x)")
    if show_grid: ax1.grid(True)

    st.pyplot(fig1)

    # ============================
    #   PLOT TURUNAN
    # ============================
    st.subheader("Plot f'(x)")
    fig2, ax2 = plt.subplots(figsize=(7, 4))

    if plot_style == "Line":
        ax2.plot(xs, yps)
    elif plot_style == "Scatter":
        ax2.scatter(xs, yps, s=10)
    else:
        ax2.plot(xs, yps)
        ax2.scatter(xs, yps, s=10)

    ax2.set_title("f'(x)")
    ax2.set_xlabel("x")
    ax2.set_ylabel("f'(x)")
    if show_grid: ax2.grid(True)

    st.pyplot(fig2)

    st.success("Berhasil menampilkan fungsi dan turunannya!")

except SympifyError:
    st.error("❌ Fungsi tidak valid. Gunakan ekspresi matematika yang benar.")
except Exception as e:
    st.error(f"Terjadi error: {e}")

