# 🚀 Panduan Upload ke GitHub

Ikuti langkah-langkah berikut untuk mengupload project ke GitHub:

## Langkah 1: Buat Repository di GitHub

1. Buka https://github.com dan login
2. Klik tombol **"+"** di pojok kanan atas → pilih **"New repository"**
3. Isi nama repository (contoh: `UAS_ML` atau `adaptabilitas-mahasiswa`)
4. Pilih **Public** atau **Private** sesuai kebutuhan
5. **JANGAN centang** "Initialize with README" (karena kita sudah punya)
6. Klik **"Create repository"**

## Langkah 2: Inisialisasi Git di Local

Jalankan perintah berikut di terminal (sudah di folder C:\UAS_ML):

```bash
git init
git add .
git commit -m "Initial commit: Aplikasi Analisis Adaptabilitas Belajar Mahasiswa"
```

## Langkah 3: Hubungkan dengan GitHub

Ganti `USERNAME` dan `REPOSITORY_NAME` dengan milik Anda:

```bash
git remote add origin https://github.com/USERNAME/REPOSITORY_NAME.git
git branch -M main
git push -u origin main
```

Contoh jika username Anda `johndoe` dan repo `uas-ml`:
```bash
git remote add origin https://github.com/johndoe/uas-ml.git
git branch -M main
git push -u origin main
```

## Catatan Penting

- Jika diminta login, GitHub sekarang menggunakan **Personal Access Token** (bukan password)
- Untuk membuat token: GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic) → Generate new token
- Berikan permission: `repo` (full control)

---

**Atau gunakan script otomatis di bawah ini!**

