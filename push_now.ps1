# Script untuk Push ke Repository UAS-MachineLearning

Write-Host "🚀 Push ke GitHub - Repository: UAS-MachineLearning" -ForegroundColor Green
Write-Host ""

# Minta username GitHub
$username = Read-Host "Masukkan username GitHub Anda"

if ([string]::IsNullOrWhiteSpace($username)) {
    Write-Host "❌ Username tidak boleh kosong!" -ForegroundColor Red
    exit 1
}

$repoName = "UAS-MachineLearning"
$remoteUrl = "https://github.com/$username/$repoName.git"

Write-Host ""
Write-Host "📝 Menambahkan semua file..." -ForegroundColor Yellow
git add .

Write-Host "💾 Membuat commit..." -ForegroundColor Yellow
$commitMessage = "Initial commit: Aplikasi Analisis Adaptabilitas Belajar Mahasiswa"
git commit -m $commitMessage

if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  Commit mungkin sudah ada atau tidak ada perubahan. Melanjutkan..." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "🔗 Mengupdate remote repository..." -ForegroundColor Yellow
git remote remove origin 2>$null
git remote add origin $remoteUrl

Write-Host "🌿 Memastikan branch main..." -ForegroundColor Yellow
git branch -M main

Write-Host ""
Write-Host "✅ Siap untuk push!" -ForegroundColor Green
Write-Host ""
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host "📤 Repository: $remoteUrl" -ForegroundColor White
Write-Host "=" * 60 -ForegroundColor Cyan
Write-Host ""
Write-Host "🚀 Push ke GitHub dengan perintah:" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor White
Write-Host ""
Write-Host "💡 Saat diminta login:" -ForegroundColor Yellow
Write-Host "   - Username: $username" -ForegroundColor White
Write-Host "   - Password: Personal Access Token (bukan password GitHub!)" -ForegroundColor White
Write-Host ""

$push = Read-Host "Apakah Anda ingin push sekarang? (Y/N)"
if ($push -eq "Y" -or $push -eq "y") {
    Write-Host ""
    Write-Host "📤 Pushing ke GitHub..." -ForegroundColor Yellow
    git push -u origin main
}

