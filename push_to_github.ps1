# Script Helper untuk Push ke GitHub
# Ganti USERNAME dan REPOSITORY_NAME dengan milik Anda

Write-Host "🚀 Persiapan Upload ke GitHub" -ForegroundColor Green
Write-Host ""

$username = Read-Host "Masukkan username GitHub Anda"
$repoName = Read-Host "Masukkan nama repository GitHub (contoh: UAS_ML)"

Write-Host ""
Write-Host "📝 Menambahkan file ke Git..." -ForegroundColor Yellow
git add .

Write-Host "💾 Membuat commit..." -ForegroundColor Yellow
git commit -m "Initial commit: Aplikasi Analisis Adaptabilitas Belajar Mahasiswa"

Write-Host ""
Write-Host "🔗 Menghubungkan dengan GitHub..." -ForegroundColor Yellow
git remote add origin "https://github.com/$username/$repoName.git" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  Remote origin sudah ada. Menghapus dan menambahkan ulang..." -ForegroundColor Yellow
    git remote remove origin
    git remote add origin "https://github.com/$username/$repoName.git"
}

Write-Host "🌿 Mengatur branch main..." -ForegroundColor Yellow
git branch -M main

Write-Host ""
Write-Host "✅ Siap untuk push!" -ForegroundColor Green
Write-Host ""
Write-Host "📤 Push ke GitHub dengan perintah:" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor White
Write-Host ""
Write-Host "💡 Jika diminta login, gunakan Personal Access Token (bukan password)" -ForegroundColor Yellow

