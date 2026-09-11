# LAB-AP-2-2026

Repositori Tugas Praktikum Algoritma dan Pemrograman 2026.

## Persiapan

1. Buat akun GitHub: <https://github.com/>
2. Install Git: <https://git-scm.com/>

## Alur Pengumpulan Tugas

1. Fork repositori ini.
2. Clone hasil fork:

   ```bash
   git clone https://github.com/YOUR_USERNAME/LAB-AP-2-2026.git
   ```

3. Masuk ke folder hasil clone, buat branch dengan nama NIM, lalu atur identitas Git:

   ```bash
   cd LAB-AP-2-2026
   git branch NIM_ANDA
   git checkout NIM_ANDA
   git config user.name USERNAME_GITHUB
   git config user.email EMAIL_GITHUB
   ```

4. Buat folder NIM Anda, lalu masuk ke dalamnya:

   ```bash
   mkdir NIM_ANDA
   cd NIM_ANDA
   ```

5. Di dalam folder NIM, buat folder `Praktikum-n` (n = nomor praktikum), lalu masuk:

   ```bash
   mkdir "Praktikum-n"
   cd "Praktikum-n"
   ```

   Contoh: `Praktikum-1`

6. Simpan semua file tugas praktikum ke folder `Praktikum-n` dengan format nama:

   ```text
   TPn_noSoal_NIM.py
   ```

   Contoh: `TP1_1_H071201068.py`, `TP2_3_H071201068.py`

7. Setiap ada perubahan, lakukan `add`, cek status, lalu commit dengan pesan deskriptif:

   ```bash
   git add "NIM_ANDA/Praktikum-n/NamaFile.py"
   git status
   git commit -m "pesan mengenai penambahan atau perubahan"
   ```

   Disarankan **tidak** menggunakan `git add .` agar file yang tidak diinginkan tidak ikut ter-commit.

8. Setelah asistensi dan tugas disetujui, push branch NIM Anda:

   ```bash
   git push origin NIM_ANDA
   ```

9. Buka repo hasil fork Anda di GitHub, pastikan perubahan sudah benar, lalu buat Pull Request.

## Jika Diminta Login saat Push

Gunakan:

- Username: username GitHub Anda
- Password: personal access token (PAT) Anda

Cara membuat PAT:

1. Klik profile (kanan atas GitHub)
2. Pilih **Settings**
3. Scroll ke bawah pilih **Developer settings**
4. Pilih **Personal access tokens**
5. Pilih **Generate new token**
6. Isi catatan token (misal: `Token for LAB-AP-2-2026`)
7. Atur masa berlaku token
8. Centang scope `repo`
9. Klik **Generate new token**
10. Salin token dan simpan (token hanya ditampilkan sekali)

## Hal yang Harus Diperhatikan

- Cara mengumpulkan tugas harus sesuai aturan di atas.
- Satu praktikum, satu folder.
- Satu soal, satu class.
- Program harus berjalan dengan baik dan benar sesuai ketentuan tugas.
