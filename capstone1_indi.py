from prettytable import PrettyTable

data_buku = PrettyTable()

# Menentukan nama kolom
data_buku.field_names = ["id", "judul", "pengarang", "penerbit", "terbit", "status"]

data_buku.add_row(["B01", "Akuntansi Pengantar 1", "Supardi", "Gava Media", 2009, "Tersedia"])
data_buku.add_row(["B02", "Patologi Sosial I", "kartini Kartono", "Sagung Seto", 2002, "Dipinjam"])
data_buku.add_row(["B03", "Ilmu Dakwah", "Dr.Moh.Ali Aziz,M.AG", "Kencana", 2016, "Tersedia"])
data_buku.add_row(["B04", "Nietzsche", "St. Sunardi", "LKis", 2011, "Dipinjam"])
data_buku.add_row(["B05", "Semantic Search", "Riyanarto Sarno", "Andi", 2012, "Tersedia"])
data_buku.add_row(["B06", "General Psychology", "C. George Boeree", "Primasophie", 2016, "Tersedia"])
data_buku.add_row(["B07", "Filsafat Ilmu", "Zaprulkhan", "Rajawali Pers", 2016, "Tersedia"])

# Membuat fungsi untuk menampilkan buku
def tampil_buku():
    if not data_buku:
        print("Tidak ada buku yang tersedia.")
    else:
        print("\n" + "*"*30)
        print(" "*8 +"DAFTAR BUKU" +" "*8)
        print("*"*30)
        print(data_buku)

# Membuat fungsi untuk cari buku
def cari_buku():
    print("\n" + "*"*30)
    print(" "*8 +"MENCARI BUKU")
    print("*"*30)
    kata_kunci = input("Masukkan kata kunci judul buku yang ingin dicari: ")
    ## MENCARI BUKU YANG MENGANDUNG KATA KUNCI
    hasil = PrettyTable()
    hasil.field_names = data_buku.field_names
    for row in data_buku._rows:
        if kata_kunci.lower() in row[1].lower():
            hasil.add_row(row)

    # Menampilkan hasil pencarian
    if not hasil._rows:
        print("Buku tidak ditemukan!")
    else:
        print("Buku yang ditemukan: ")
        print(hasil)

# Fungsi menambahkan buku
def tambah_buku(item):    
    # Cek jika item sudah ada di dalam daftar
    for row in data_buku._rows:
        if item == row[0]:
            print(f"Buku dengan ID {item} sudah ada di dalam daftar buku.")
            return
    # Input dari pengguna
    judul = input("Masukkan judul buku: ")
    pengarang = input("Masukkan nama pengarang: ")
    penerbit = input("Masukkan nama penerbit: ")

    # Menerapkan try...except untuk menangkap kesalahan saat mengonversi ke integer
    while True:
        try:
            terbit = int(input("Masukkan tahun terbit: "))
            if terbit < 1900:
                print("Tahun terbit harus di atas tahun 1900")
            else:
                break
        except ValueError:
            print("Tahun terbit harus berupa angka.")

    status = "Tersedia"

    # Menampilkan tabel yang telah diinput namun belum disimpan
    konfirmasi_tambah = PrettyTable()
    konfirmasi_tambah.add_row([item, judul, pengarang, penerbit, terbit, status])
    konfirmasi_tambah.field_names = data_buku.field_names
    print(konfirmasi_tambah)
    
    # Fungsi konfirmasi ulang ke user untuk menyimpan data
    konfirmasi = input(f"Apakah Anda yakin akan menyimpan data tersebut? (y/n): ")
    if konfirmasi.lower() == 'y':
        ## MENYIMPAN DATA
        data_buku.add_row([item, judul, pengarang, penerbit, terbit, status])
        print(f"Buku dengan judul {judul} berhasil ditambahkan.")
    else:
        print("Penambahan buku dibatalkan.")

def ubah_buku():
    print("\n" + "*"*30)
    print(" "*2 +"MENGUBAH INFORMASI BUKU")
    print("*"*30)
    id_buku = input("Masukkan ID buku yang ingin diperbarui: ").upper()
    buku = cari_by_id(id_buku)
    if buku:
        tabel_pilih(buku)
        print("Pilih kolom yang ingin diubah:")
        for i, kolom in enumerate(data_buku.field_names):
            print(f"{i + 1}. {kolom}")

        while True:
            try:
                pilihan_kolom = int(input("Masukkan nomor kolom: "))
                if 1 <= pilihan_kolom <= len(data_buku.field_names):
                    break
                else:
                    print("Nomor kolom tidak valid.")
            except ValueError:
                print("Masukkan angka yang valid.")

        if pilihan_kolom == 1:
            id_baru = input("Masukkan ID buku terbaru: ").upper()
            print(f"ID buku akan diubah menjadi: {id_baru}")
            #update data statistik peminjaman
            if id_buku in peminjaman_statistik:
                peminjaman_statistik[id_baru] = peminjaman_statistik.pop(id_buku,0)
        elif pilihan_kolom == 2:
            judul_baru = input("Masukkan judul buku terbaru: ")
            print(f"Judul buku akan diubah menjadi: {judul_baru}")
        elif pilihan_kolom == 3:
            pengarang_baru = input("Masukkan nama pengarang terbaru: ")
            print(f"Nama pengarang akan diubah menjadi: {pengarang_baru}")
        elif pilihan_kolom == 4:
            penerbit_baru = input("Masukkan nama penerbit terbaru: ")
            print(f"Nama penerbit akan diubah menjadi: {penerbit_baru}")
        elif pilihan_kolom == 5:
            while True:
                try:
                    terbit_baru = int(input("Masukkan tahun terbit terbaru: "))
                    if terbit_baru < 1900:
                        print("Tahun terbit harus di atas tahun 1900")
                    else:
                        break
                except ValueError:
                    print("Masukkan angka yang valid.")
            print(f"Tahun terbit akan diubah menjadi: {terbit_baru}")
        elif pilihan_kolom == 6:
            while True:
                status_baru = input("Masukkan status terbaru (Tersedia/Dipinjam): ").title()
                if status_baru in ['Tersedia', 'Dipinjam']:
                    if buku[5] == 'Dipinjam' and status_baru == 'Tersedia':
                        # Use get to provide a default value of 0 if the key doesn't exist
                        peminjaman_statistik[id_buku] = peminjaman_statistik.get(id_buku, 0) - 1
                    elif buku[5] == 'Tersedia' and status_baru == 'Dipinjam':
                        peminjaman_statistik[id_buku] = peminjaman_statistik.get(id_buku, 0) + 1
                    break
                else:
                    print("Status baru harus diisi dengan Tersedia atau Dipinjam")
            print(f"Status akan diubah menjadi: {status_baru}")

        else:
            print("Tidak ada perubahan yang dilakukan.")
            return

        konfirmasi = input("Apakah Anda yakin ingin menyimpan perubahan? (y/n): ")
        if konfirmasi.lower() == 'y':
            buku[0] = id_baru if pilihan_kolom == 1 else buku[0]
            buku[1] = judul_baru if pilihan_kolom == 2 else buku[1]
            buku[2] = pengarang_baru if pilihan_kolom == 3 else buku[2]
            buku[3] = penerbit_baru if pilihan_kolom == 4 else buku[3]
            buku[4] = terbit_baru if pilihan_kolom == 5 else buku[4]
            buku[5] = status_baru if pilihan_kolom == 6 else buku[5]
            print(f"Buku dengan ID {id_buku} berhasil diperbarui.")
        else:
            print("Perubahan dibatalkan.")
    else:
        print("Buku tidak ditemukan.")

def hapus_buku():
    print("\n" + "*"*30)
    print(" "*8 +"MENGHAPUS BUKU")
    print("*"*30)
    id_buku = input("Masukkan ID buku yang ingin dihapus: ").upper()
    buku = cari_by_id(id_buku)

    if buku:
        # Menampilkan informasi buku yang akan dihapus
        tabel_pilih(buku)
        # Konfirmasi pengguna
        konfirmasi = input(f"Apakah Anda yakin ingin menghapus buku dengan ID {id_buku}? (y/n): ")
        if konfirmasi.lower() == 'y':
            data_buku._rows.remove(buku) 
            print(f"Buku dengan ID {id_buku} berhasil dihapus.")
        else:
            print("Penghapusan buku dibatalkan.")
    else:
        print("Buku tidak ditemukan.")

def find_last_book_id():
    # Extract numeric part from each book ID, convert to integers, and find the maximum
    numeric_ids = [int(row[0][1:]) for row in data_buku._rows]
    return f"B{max(numeric_ids):02d}" if numeric_ids else "B00"

def tabel_pilih(buku):
    tabel_pilih = PrettyTable()
    tabel_pilih.add_row(buku)
    tabel_pilih.field_names = data_buku.field_names
    print(tabel_pilih)

# Dictionary untuk melacak status peminjaman setiap buku
peminjaman_statistik = {}

def pinjam_buku():
    print("\n" + "*"*30)
    print(" "*8 +"MEMINJAM BUKU")
    print("*"*30)
    id_buku = input("Masukkan ID buku yang ingin dipinjam: ").upper()
    buku = cari_by_id(id_buku)

    if buku:
        tabel_pilih(buku)
        if buku[5] == 'Tersedia':
            # Ask for confirmation
            konfirmasi = input(f"Apakah Anda yakin ingin meminjam buku dengan ID {id_buku}? (y/n): ")
            if konfirmasi.lower() == 'y':
                buku[5] = 'Dipinjam'
                # Menambahkan statistik peminjaman
                peminjaman_statistik[id_buku] = peminjaman_statistik.get(id_buku, 0) + 1
                print(f"Buku dengan ID Buku {id_buku} berhasil dipinjam.")
            else:
                print("Peminjaman buku dibatalkan.")
        else:
            print("Buku tidak tersedia untuk dipinjam.")
    else:
        print("Buku tidak ditemukan.")

def kembali_buku():
    print("\n" + "*"*30)
    print(" "*5 +"MENGEMBALIKAN BUKU")
    print("*"*30)
    id_buku = input("Masukkan ID buku yang ingin dikembalikan: ").upper()
    buku = cari_by_id(id_buku)
    if buku:
        tabel_pilih(buku)
        if buku[5] == 'Dipinjam':
            # konfirmasi
            konfirmasi = input(f"Apakah Anda yakin ingin mengembalikan buku dengan ID {id_buku}? (y/n): ")
            if konfirmasi.lower() == 'y':
                buku[5] = 'Tersedia'
                print(f"Buku dengan ID Buku {id_buku} berhasil dikembalikan.")
                
            else:
                print("Pengembalian buku dibatalkan")
        else:
            print("Buku sudah tersedia atau tidak sedang dipinjam.")
    else:
        print("Buku tidak ditemukan.")

def daftar_statistik_peminjaman():
    if not peminjaman_statistik:
        print("Belum ada data statistik peminjaman.")
    else:
        print("\n" + "*"*30)
        print(" "*2 +"STATISTIK PEMINJAMAN BUKU")
        print("*"*30)
        for id_buku, jumlah_peminjaman in peminjaman_statistik.items():
            buku = cari_by_id(id_buku)
            if buku:
                print(f"Judul: {buku[1]}, Jumlah Peminjaman : {jumlah_peminjaman} ")

# Fungsi untuk mencari buku berdasarkan ID
def cari_by_id(id_buku):
    for row in data_buku._rows:
        if id_buku == row[0]:
            return row
    return None

while True:
    print("\n" + "="*47)
    print(" "*5 + "SISTEM INFORMASI PEMINJAMAN BUKU")
    print("-"*47)
    print('''    Sistem Informasi Peminjaman Buku ini 
    memungkinkan Admin untuk:
    - Melihat daftar buku yang tersedia;
    - Menambahkan buku baru ke dalam sistem;
    - Mengupdate informasi buku yang ada;
    - Menghapus buku dari perpustakaan;
    - Melakukan peminjaman dan pengembalian 
      dan statistik peminjaman buku.''')
    print("="*47)
    print("1. Menu Daftar Buku")
    print("2. Menu Tambah Buku")
    print("3. Menu Perbarui Informasi Buku")
    print("4. Menu Hapus Buku")
    print("5. Menu Peminjaman Buku")
    print("6. Keluar")
    print("="*47 + "\n")

    choice = input("Masukkan pilihan Anda (1-6): ")

    if choice == '1':
        while True:
            print("\n" + "="*30)
            print(" "*4 + "SUBMENU DAFTAR BUKU")
            print("="*30)
            print("1. Lihat Semua Buku")
            print("2. Cari Buku")
            print("3. Kembali ke Menu Utama")
            print("="*30 + "\n")

            sub_menu = input("Masukkan pilihan Anda (1-3): ")
            
            if sub_menu == '1':
                tampil_buku()
            elif sub_menu == '2':
                cari_buku()
            elif sub_menu == '3':
                break
            else:
                print("Pilihan tidak valid. Masukkan angka antara 1-3.")
    
        
    elif choice == '2':
         while True:
            print("\n" + "="*30)
            print(" "*4 + "SUBMENU TAMBAH BUKU")
            print("="*30)
            print("1. Tambah Buku")
            print("2. Kembali ke Menu Utama")
            print("="*30 + "\n")

            sub_menu = input("Masukkan pilihan Anda (1-2): ")
            
            if sub_menu == '1':
                last_id = find_last_book_id()
                print("\n" + "*"*30)
                print(" "*8 +"MENAMBAH BUKU")
                print("*"*30)
                item = input(f"Masukkan id buku (ID Buku terakhir {last_id}): ")
                tambah_buku(item.upper())
            elif sub_menu == '2':
                break
            else:
                print("Pilihan tidak valid. Masukkan angka antara 1-2.")
        
    elif choice == '3':
        while True:
            print("\n" + "="*30)
            print(" "*4 + "SUBMENU PERBARUI INFORMASI BUKU")
            print("="*30)
            print("1. Perbarui Informasi Buku")
            print("2. Kembali ke Menu Utama")
            print("="*30 + "\n")

            sub_menu = input("Masukkan pilihan Anda (1-2): ")
            
            if sub_menu == '1':
                ubah_buku()
            elif sub_menu == '2':
                break
            else:
                print("Pilihan tidak valid. Masukkan angka antara 1-2.")     

    elif choice == '4':
        while True:
            print("\n" + "="*30)
            print(" "*4 + "SUBMENU HAPUS BUKU")
            print("="*30)
            print("1. Hapus Informasi Buku")
            print("2. Kembali ke Menu Utama")
            print("="*30 + "\n")

            sub_menu = input("Masukkan pilihan Anda (1-2): ")
            
            if sub_menu == '1':
                hapus_buku()
            elif sub_menu == '2':
                break
            else:
                print("Pilihan tidak valid. Masukkan angka antara 1-2.")  
                
    elif choice == '5':
        while True:
            print("\n" + "="*30)
            print(" "*4 + "SUBMENU PEMINJAMAN BUKU")
            print("="*30)
            print("1. Pinjam Buku")
            print("2. Kembalikan Buku")
            print("3. Statistik Peminjaman Buku")
            print("4. Kembali ke Menu Utama")
            print("="*30 + "\n")

            sub_menu = input("Masukkan pilihan (1-4): ")

            if sub_menu == '1':
                pinjam_buku()
            elif sub_menu == '2':
                kembali_buku()
            elif sub_menu == '3':
                daftar_statistik_peminjaman()
            elif sub_menu == '4':
                break
            else:
                print("Pilihan tidak valid. Masukkan angka antara 1-4.")
 
    elif choice == '6':
        print("Terima kasih telah menggunakan program kami. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Masukkan angka antara 1-6.")
