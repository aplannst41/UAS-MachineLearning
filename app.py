import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# ==========================================
# 1. KONFIGURASI HALAMAN (Wajib di baris pertama)
# ==========================================
st.set_page_config(
    page_title="Adaptabilitas Mahasiswa",
    page_icon="🎓",
    layout="centered" # Bisa ganti 'wide' kalau mau lebar
)

# ==========================================
# 2. LOAD MODEL & ASSETS
# ==========================================
@st.cache_resource
def load_model():
    return joblib.load('model_adaptabilitas.pkl')

try:
    paket = load_model()
    model = paket['model']
    encoders = paket['encoders']
except FileNotFoundError:
    st.error("File 'model_adaptabilitas.pkl' tidak ditemukan. Pastikan file ada di satu folder dengan app.py")
    st.stop()

# ==========================================
# 3. UI: SIDEBAR (Untuk Input Data)
# ==========================================
with st.sidebar:
    st.header("📝 Input Data Mahasiswa")
    st.write("Silakan isi kuesioner di bawah ini:")
    
    # Kelompokkan input biar rapi
    st.subheader("1. Profil Diri")
    gender = st.radio("Jenis Kelamin", encoders['Gender'].classes_, horizontal=True)
    age = st.selectbox("Rentang Usia", encoders['Age'].classes_)
    
    st.subheader("2. Akademik")
    edu = st.selectbox("Jenjang Pendidikan", encoders['Education Level'].classes_)
    inst = st.selectbox("Tipe Institusi", encoders['Institution Type'].classes_)
    it_student = st.radio("Apakah Mahasiswa IT?", encoders['IT Student'].classes_, horizontal=True)
    
    st.subheader("3. Fasilitas & Lingkungan")
    col_sb1, col_sb2 = st.columns(2)
    with col_sb1:
        location = st.selectbox("Lokasi (Kota)", encoders['Location'].classes_)
        financial = st.selectbox("Kondisi Ekonomi", encoders['Financial Condition'].classes_)
        internet = st.selectbox("Tipe Internet", encoders['Internet Type'].classes_)
        device = st.selectbox("Perangkat Utama", encoders['Device'].classes_)

    with col_sb2:
        load_shedding = st.selectbox("Mati Listrik", encoders['Load-shedding'].classes_)
        network = st.selectbox("Jaringan (G/Wifi)", encoders['Network Type'].classes_)
        class_dur = st.selectbox("Durasi Kelas", encoders['Class Duration'].classes_)
        self_lms = st.selectbox("Punya LMS Sendiri?", encoders['Self Lms'].classes_)
        
    st.info("Pastikan semua data terisi dengan benar.")

# ==========================================
# 4. UI: HALAMAN UTAMA (Main Page)
# ==========================================

# Header Gambar (Bisa pakai URL gambar dari internet)
st.image("https://img.freepik.com/free-vector/online-learning-concept-illustration_114360-4966.jpg?w=1380", use_container_width=True)

st.title("🎓 Analisis Adaptabilitas Belajar")
st.markdown("""
Aplikasi berbasis **Machine Learning** ini berfungsi untuk mendeteksi dini tingkat kesiapan mahasiswa 
dalam menghadapi metode pembelajaran daring (*online learning*).
""")

st.divider() # Garis pemisah

# Bagian Output
st.subheader("Hasil Prediksi")

# Tombol Eksekusi
if st.sidebar.button("🔍 ANALISIS SEKARANG", type="primary"):
    
    # Animasi Loading biar keren
    with st.spinner('Sedang memproses data dengan AI...'):
        
        # Siapkan data input
        input_data = pd.DataFrame([[gender, age, edu, inst, it_student, location, 
                                    load_shedding, financial, internet, network, 
                                    class_dur, self_lms, device]],
                                columns=['Gender', 'Age', 'Education Level', 'Institution Type', 'IT Student', 'Location', 
                                        'Load-shedding', 'Financial Condition', 'Internet Type', 'Network Type', 
                                        'Class Duration', 'Self Lms', 'Device'])
        
        # Encode data
        for col in input_data.columns:
            input_data[col] = encoders[col].transform(input_data[col])
        
        # Prediksi
        hasil_angka = model.predict(input_data)
        hasil_teks = encoders['Adaptivity Level'].inverse_transform(hasil_angka)[0]
        
        # Tampilkan Hasil dengan Gaya
        st.success("Analisis Selesai!")
        
        col_res1, col_res2 = st.columns([1, 2])
        
        with col_res1:
            # Tampilkan metrik besar
            st.metric(label="Status Adaptabilitas", value=hasil_teks)
            
        with col_res2:
            # Penjelasan detail berdasarkan hasil
            if hasil_teks == 'High':
                st.balloons() # Efek balon
                st.markdown("### 🌟 Sangat Siap (High)")
                st.write("Mahasiswa ini memiliki fasilitas dan kondisi yang sangat mendukung.")
            
            elif hasil_teks == 'Moderate':
                st.markdown("### 😐 Cukup Siap (Moderate)")
                st.write("Mahasiswa ini cukup mampu mengikuti, namun perlu perhatian pada kestabilan jaringan.")
                
            else: # Low
                st.error("⚠️ Perlu Bantuan (Low)")
                st.write("**Rekomendasi:** Dosen Wali disarankan segera menghubungi mahasiswa ini untuk memberikan solusi alternatif.")

else:
    st.info("👈 Silakan masukkan data di menu sebelah kiri, lalu tekan tombol **Analisis Sekarang**.")