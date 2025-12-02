# 🚪 Cara Logout dari GitHub di Windows

Ada beberapa cara untuk logout dari GitHub, tergantung bagaimana Anda login sebelumnya:

---

## 🔑 Metode 1: Logout dari Windows Credential Manager (Paling Umum)

Git di Windows biasanya menyimpan credential di **Windows Credential Manager**.

### Cara 1: Melalui Windows Settings

1. Tekan `Windows + R` untuk membuka Run
2. Ketik: `control /name Microsoft.CredentialManager`
3. Klik **"Windows Credentials"**
4. Cari entry yang berisi:
   - `git:https://github.com`
   - Atau `github.com`
5. Klik **"Remove"** atau **"Edit"** lalu hapus password

### Cara 2: Melalui Command Prompt (Terminal)

**Hapus credential GitHub:**
```powershell
cmdkey /list:git:https://github.com
```

Jika ada, hapus dengan:
```powershell
cmdkey /delete:git:https://github.com
```

**Atau hapus semua credential GitHub:**
```powershell
cmdkey /list | Select-String "github"
```

Kemudian hapus satu per satu:
```powershell
cmdkey /delete:TargetName
```

---

## 🔑 Metode 2: Logout dari Git Credential Helper

### Hapus credential dari Git:

```powershell
git credential reject
```

Kemudian ketik:
```
protocol=https
host=github.com
```

Tekan `Enter` dua kali.

### Atau gunakan perintah langsung:

```powershell
echo "protocol=https`nhost=github.com`n" | git credential reject
```

---

## 🔑 Metode 3: Reset Git Credential Helper

### Hapus credential helper:

```powershell
git config --global --unset credential.helper
```

**Atau reset ke default:**
```powershell
git config --global credential.helper manager-core
```

---

## 🔑 Metode 4: Logout dari GitHub CLI (Jika Menggunakan)

Jika Anda menggunakan GitHub CLI (`gh`):

```powershell
gh auth logout
```

---

## 🔑 Metode 5: Hapus Manual dari Credential Manager

### Langkah Detail:

1. Buka **Control Panel**
2. Pilih **"Credential Manager"** atau **"Windows Credentials"**
3. Di bagian **"Generic Credentials"**:
   - Cari `git:https://github.com`
   - Atau cari entry yang mengandung "github"
4. Klik entry tersebut
5. Pilih **"Remove"** atau **"Edit"** untuk menghapus password

### Atau melalui PowerShell:

```powershell
# List semua credential
cmdkey /list

# Hapus credential GitHub
cmdkey /delete:git:https://github.com
```

---

## ✅ Verifikasi Logout Berhasil

Coba push/pull dari GitHub, seharusnya akan diminta login lagi:

```powershell
git ls-remote https://github.com/USERNAME/REPO.git
```

Jika diminta username dan password, berarti logout berhasil! 🎉

---

## 🔄 Cara Login Lagi

Setelah logout, saat push/pull, Git akan meminta credential lagi:

1. **Username**: username GitHub Anda
2. **Password**: gunakan **Personal Access Token** (bukan password GitHub)

### Buat Personal Access Token:
1. GitHub → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token
4. Beri permission: `repo`
5. Copy token dan gunakan sebagai password

---

## 🆘 Troubleshooting

**Credential masih tersimpan?**
- Coba hapus dari Windows Credential Manager secara manual
- Restart terminal/PowerShell setelah menghapus

**Masih bisa push tanpa diminta password?**
- Credential mungkin tersimpan di lokasi lain
- Cek semua metode di atas

**Ingin logout dari browser GitHub?**
- Buka https://github.com
- Klik profil → Settings → Sign out

---

## 📝 Catatan

- Logout dari Git **TIDAK** sama dengan logout dari browser GitHub
- Credential Git hanya mempengaruhi akses melalui Git command line
- Untuk logout dari website GitHub, lakukan dari browser

