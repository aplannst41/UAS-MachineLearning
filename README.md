# 🎓 Aplikasi Analisis Adaptabilitas Belajar Mahasiswa

Aplikasi berbasis **Machine Learning** menggunakan Streamlit untuk mendeteksi dini tingkat kesiapan mahasiswa dalam menghadapi metode pembelajaran daring (*online learning*).

## 📋 Deskripsi

Aplikasi ini menggunakan model **Random Forest Classifier** untuk menganalisis berbagai faktor yang mempengaruhi adaptabilitas mahasiswa dalam pembelajaran online, seperti:

- Profil Diri (Jenis Kelamin, Usia)
- Faktor Akademik (Jenjang Pendidikan, Tipe Institusi, Jurusan IT)
- Fasilitas & Lingkungan (Lokasi, Kondisi Ekonomi, Tipe Internet, Perangkat, dll)

Hasil analisis akan mengklasifikasikan mahasiswa ke dalam 3 kategori:
- **High** - Sangat Siap
- **Moderate** - Cukup Siap  
- **Low** - Perlu Bantuan

## 🚀 Cara Menjalankan

### Prasyarat

- Python 3.8 atau lebih tinggi
- pip (Python package manager)

### Instalasi

1. Clone repository ini:
```bash
git clone <URL_REPOSITORY_ANDA>
cd UAS_ML
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Pastikan file `model_adaptabilitas.pkl` ada di folder yang sama dengan `app.py`

4. Jalankan aplikasi:
```bash
streamlit run app.py
```

5. Buka browser dan akses `http://localhost:8501`

## 📦 Dependencies

- streamlit >= 1.28.0
- pandas >= 1.5.0
- joblib >= 1.3.0
- Pillow >= 9.0.0
- scikit-learn (untuk model)

## 📁 Struktur Project

```
UAS_ML/
├── app.py                      # Aplikasi Streamlit utama
├── model_adaptabilitas.pkl     # Model machine learning
├── requirements.txt            # Dependencies Python
├── README.md                   # Dokumentasi
└── .gitignore                  # File yang diabaikan oleh Git
```

## 🎯 Cara Menggunakan

1. Buka aplikasi di browser
2. Isi kuesioner di sidebar sebelah kiri:
   - Profil Diri (Jenis Kelamin, Usia)
   - Data Akademik (Jenjang, Institusi, Jurusan)
   - Fasilitas & Lingkungan (Internet, Perangkat, dll)
3. Klik tombol **"🔍 ANALISIS SEKARANG"**
4. Lihat hasil prediksi adaptabilitas mahasiswa

## 🔧 Teknologi yang Digunakan

- **Frontend**: Streamlit
- **Machine Learning**: scikit-learn (Random Forest Classifier)
- **Data Processing**: pandas
- **Model Persistence**: joblib

## 📝 Catatan

- Model ini dilatih dengan scikit-learn version 1.6.1
- Pastikan semua field diisi sebelum melakukan analisis
- File model (`model_adaptabilitas.pkl`) diperlukan untuk menjalankan aplikasi

## 👤 Author

Dibuat untuk keperluan UAS Machine Learning

## 📄 License

Project ini dibuat untuk keperluan akademik.

