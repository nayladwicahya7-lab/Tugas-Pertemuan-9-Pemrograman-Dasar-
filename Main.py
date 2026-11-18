"""Program utama untuk demonstrasi modularisasi fungsi pengolah suhu harian.

Simpan file ini satu folder dengan cuaca.py, kemudian jalankan:
    python main.py
"""

from cuaca import (
    hitung_rata_rata,
    cari_suhu_minimum,
    cari_suhu_maksimum,
    hitung_rentang,
    klasifikasi_suhu,
)


def tampilkan_ringkasan(nama_kota, data_suhu):
    """Menampilkan ringkasan statistik suhu untuk satu kota.

    Fungsi ini menggunakan fungsi-fungsi reusable dari modul cuaca.
    """
    print("\n" + "=" * 54)
    print(f"RINGKASAN SUHU HARIAN: {nama_kota}")
    print("=" * 54)
    print("Data suhu (°C):", data_suhu)

    rata_rata = hitung_rata_rata(data_suhu)
    minimum = cari_suhu_minimum(data_suhu)
    maksimum = cari_suhu_maksimum(data_suhu)
    rentang = hitung_rentang(data_suhu)

    if rata_rata is None:
        print("Tidak ada data untuk dihitung.")
        return

    print("Jumlah hari :", len(data_suhu))
    print(f"Rata-rata   : {rata_rata:.2f} °C")
    print("Minimum     :", minimum, "°C")
    print("Maksimum    :", maksimum, "°C")
    print("Rentang     :", rentang, "°C")
    print("Kategori rata-rata:", klasifikasi_suhu(rata_rata))


def demo_klasifikasi():
    """Menunjukkan fungsi klasifikasi pada suhu normal dan nilai batas."""
    print("\n" + "=" * 54)
    print("DEMO KLASIFIKASI SUHU")
    print("=" * 54)

    daftar_uji = [18, 22, 23, 27, 28, 32, 33, 60]
    for suhu in daftar_uji:
        print(f"Suhu {suhu:>3} °C -> {klasifikasi_suhu(suhu)}")


def main():
    """Menjalankan demonstrasi program utama."""
    print("PEMROGRAMAN DASAR UNTUK SAINS DATA")
    print("FUNCTION DAN MODULARISASI — STUDI KASUS SUHU HARIAN")

    # Dataset sederhana: data yang berbeda menggunakan fungsi yang sama.
    kota_a = [31, 33, 34, 32, 30, 35, 33]
    kota_b = [18, 20, 19, 22, 21, 17, 20]
    kota_c = []

    tampilkan_ringkasan("Kota A (dataran rendah)", kota_a)
    tampilkan_ringkasan("Kota B (dataran tinggi)", kota_b)
    tampilkan_ringkasan("Kota C (belum ada data)", kota_c)
    demo_klasifikasi()

    print("\nDemonstrasi selesai.")
    print("Perhatikan: main.py mengatur alur, sedangkan cuaca.py")
    print("menyediakan fungsi yang dapat dipakai kembali.")


if __name__ == "__main__":
    main()