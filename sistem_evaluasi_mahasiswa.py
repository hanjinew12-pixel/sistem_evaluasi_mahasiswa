nilai_tugas = 90
nilai_uts = 85
nilai_uas = 85
kehadiran = 90

nilai_akhir = (0.2 * nilai_tugas) + (0.3 * nilai_uts) + (0.5 * nilai_uas)

if nilai_akhir >= 85 and kehadiran >= 90 and int(nilai_akhir) % 2 == 0:
    status = "LULUS DENGAN PREDIKAT"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "LULUS"
else:
    status = "BELUM LULUS"

print(f"Nilai Akhir: {int(nilai_akhir)}")
print(f"Status: {status}")

print("=================================")
nilai_tugas = 90
nilai_uts = 75
nilai_uas = 80
kehadiran = 80

nilai_akhir = (0.2 * nilai_tugas) + (0.3 * nilai_uts) + (0.5 * nilai_uas)

if nilai_akhir >= 85 and kehadiran >= 90 and int(nilai_akhir) % 2 == 0:
    status = "LULUS DENGAN PREDIKAT"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "LULUS"
else:
    status = "BELUM LULUS"

print(f"Nilai Akhir: {int(nilai_akhir)}")
print(f"Status: {status}")

print("================================")
nilai_tugas = 75
nilai_uts = 75
nilai_uas = 75
kehadiran = 75

nilai_akhir = (0.2 * nilai_tugas) + (0.3 * nilai_uts) + (0.5 * nilai_uas)

if nilai_akhir >= 85 and kehadiran >= 90 and int(nilai_akhir) % 2 == 0:
    status = "LULUS DENGAN PREDIKAT"
elif nilai_akhir >= 75 and kehadiran >= 80:
    status = "LULUS"
else:
    status = "BELUM LULUS"

print(f"Nilai Akhir: {int(nilai_akhir)}")
print(f"Status: {status}"
