# 📤 Cara Upload ke GitHub - Langkah Lengkap

## ⚡ Cara Cepat (Menggunakan Script)

1. **Buat Repository di GitHub terlebih dahulu:**
   - Buka https://github.com
   - Klik **"+"** → **"New repository"**
   - Nama: `UAS_ML` (atau nama lain)
   - Pilih Public/Private
   - **JANGAN** centang "Initialize with README"
   - Klik **"Create repository"**

2. **Jalankan script helper:**
   ```powershell
   .\sh_to_github.ps1pu
   ```
   Script akan meminta username dan nama repository Anda

3. **Push ke GitHub:**
   Setelah script selesai, jalankan:
   ```powershell
   git push -u origin main
   ```

---

## 📝 Cara Manual (Step by Step)

### Langkah 1: Buat Repository di GitHub
1. Login ke https://github.com
2. Klik tombol **"+"** di pojok kanan atas
3. Pilih **"New repository"**
4. Isi nama repository (contoh: `UAS_ML`)
5. Pilih **Public** atau **Private**
6. **JANGAN centang** "Add a README file"
7. Klik **"Create repository"**

### Langkah 2: Add & Commit File
```powershell
git add .
git commit -m "Initial commit: Aplikasi Analisis Adaptabilitas Belajar"
```

### Langkah 3: Hubungkan dengan GitHub
**Ganti `USERNAME` dan `REPOSITORY_NAME` dengan milik Anda:**

```powershell
git remote add origin https://github.com/USERNAME/REPOSITORY_NAME.git
git branch -M main
```

**Contoh:**
Jika username Anda `johndoe` dan repository `uas-ml`:
```powershell
git remote add origin https://github.com/johndoe/uas-ml.git
git branch -M main
```

### Langkah 4: Push ke GitHub
```powershell
git push -u origin main
```

---

## 🔐 Login GitHub (Jika Diminta)

GitHub **tidak lagi** menerima password. Gunakan **Personal Access Token**:

### Cara Buat Token:
1. GitHub → **Settings** (icon profil di pojok kanan)
2. Scroll ke bawah → **Developer settings**
3. **Personal access tokens** → **Tokens (classic)**
4. **Generate new token (classic)**
5. Beri nama token (contoh: "Git Push Token")
6. Pilih expiration (30 days / 90 days / no expiration)
7. Centang permission: **`repo`** (full control)
8. Klik **"Generate token"**
9. **COPY TOKEN** (hanya muncul sekali!)
10. Gunakan token ini sebagai password saat push

---

## ✅ Setelah Berhasil

1. Refresh halaman repository di GitHub
2. Semua file Anda akan muncul di sana
3. URL repository: `https://github.com/USERNAME/REPOSITORY_NAME`

---

## 🆘 Troubleshooting

**Error: "remote origin already exists"**
```powershell
git remote remove origin
git remote add origin https://github.com/USERNAME/REPOSITORY_NAME.git
```

**Error: "Authentication failed"**
- Pastikan menggunakan Personal Access Token, bukan password
- Token harus memiliki permission `repo`

**Error: "Repository not found"**
- Pastikan repository sudah dibuat di GitHub
- Periksa username dan nama repository benar

---

## 📁 File yang Akan Di-upload

✅ **Akan di-upload:**
- `app.py`
- `model_adaptabilitas.pkl`
- `requirements.txt`
- `README.md`
- `.gitignore`
- `GITHUB_SETUP.md`
- `push_to_github.ps1`

❌ **Tidak akan di-upload** (ada di .gitignore):
- `__pycache__/`
- `*.pyc`
- Folder virtual environment
- File IDE

