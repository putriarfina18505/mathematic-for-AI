import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# 1. Dataset Mentah
data = {
    'No': range(1, 51),
    'IPK': [3.5, 2.8, 3.2, 2.5, 3.8, 2.9, 3.1, 3.4, np.nan, 3.6, 2.7, 3.3, 3.0, 2.4, 3.9, 3.25, 2.65, 3.15, 3.45, 2.85, 3.7, 2.55, 3.05, 3.35, 2.95, 3.55, 2.75, 3.28, np.nan, 3.65, 2.45, 3.12, 3.42, 2.88, 3.75, 2.6, 3.08, 3.38, 2.92, 3.85, 3.22, 2.72, 3.18, 3.48, 2.82, 3.62, 2.52, 3.02, 3.32, 2.98],
    'Kehadiran': [90, 75, 85, 60, 95, 70, 80, 88, 75, 92, 65, 85, np.nan, 55, 100, 82, 70, 78, 90, 72, 94, 62, 80, 87, 74, 91, 68, 84, 80, 93, 58, 79, 89, 73, 96, 63, 81, 86, 71, 98, 83, 67, np.nan, 92, 76, 95, 61, 79, 84, 74],
    'Beasiswa': ['Dapat', 'Tidak', 'Dapat', 'Tidak', 'Dapat', 'Tidak', 'Tidak', 'Dapat', 'Tidak', 'Dapat', 'Tidak', 'Dapat', 'Tidak', 'Tidak', 'Dapat', 'Dapat', 'Tidak', 'Tidak', 'Dapat', 'Tidak', 'Dapat', 'Tidak', 'Tidak', 'Dapat', 'Tidak', 'Dapat', 'Tidak', 'Dapat', 'Tidak', 'Dapat', 'Tidak', 'Tidak', 'Dapat', 'Tidak', 'Dapat', 'Tidak', 'Tidak', 'Dapat', 'Tidak', 'Dapat', 'Dapat', 'Tidak', 'Tidak', 'Dapat', 'Tidak', 'Dapat', 'Tidak', 'Tidak', 'Dapat', 'Tidak'],
    'Lulus': ['Ya', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Ya', 'Ya', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Ya', 'Ya', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Ya', 'Tidak']
}

df = pd.DataFrame(data)

# --- PREPROCESSING ---
# Isi Nilai Kosong
df['IPK'] = df['IPK'].fillna(df['IPK'].mean())
df['Kehadiran'] = df['Kehadiran'].fillna(df['Kehadiran'].mean())

# Ubah Kategori ke Angka
le = LabelEncoder()
df['Beasiswa'] = le.fit_transform(df['Beasiswa']) # Dapat=0, Tidak=1
df['Lulus'] = le.fit_transform(df['Lulus'])       # Tidak=0, Ya=1

# --- SIMPAN KE EXCEL ---
df.to_excel("data_bersih_random_forest.xlsx", index=False)

print("File 'data_bersih_random_forest.xlsx' telah berhasil dibuat!")