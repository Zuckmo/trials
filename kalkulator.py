import streamlit as st

# Judul Aplikasi
st.title("Kalkulator Sederhana dengan Streamlit")

# Input Angka
num1 = st.number_input("Masukkan angka pertama:", value=0.0)
num2 = st.number_input("Masukkan angka kedua:", value=0.0)

# Pilihan Operasi
operation = st.radio("Pilih operasi:", ("Tambah", "Kurang", "Kali", "Bagi"))

# Tombol Hitung
if st.button("Hitung"):
    if operation == "Tambah":
        result = num1 + num2          
    elif operation == "Kurang":
        result = num1 - num2
    elif operation == "Kali":
        result = num1 * num2
    elif operation == "Bagi":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Pembagian dengan nol tidak diperbolehkan"

    # Tampilkan Hasil
    st.success(f"Hasil: {result}")
