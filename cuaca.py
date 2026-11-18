"""Modul fungsi statistik dasar untuk data suhu harian.

Modul ini berisi fungsi-fungsi reusable untuk mengolah kumpulan data suhu
(dalam derajat Celsius), yaitu rata-rata, suhu minimum, suhu maksimum,
rentang suhu, dan klasifikasi kenyamanan suhu.
"""


def hitung_rata_rata(data):
    """Menghitung rata-rata dari kumpulan suhu.

    Args:
        data (list): Kumpulan suhu (derajat Celsius).

    Returns:
        float | None: Suhu rata-rata. Mengembalikan None jika data kosong.
    """
    if len(data) == 0:
        return None

    return sum(data) / len(data)


def cari_suhu_minimum(data):
    """Mengembalikan suhu terendah dari kumpulan suhu.

    Args:
        data (list): Kumpulan suhu yang akan diperiksa.

    Returns:
        int | float | None: Suhu terendah, atau None jika data kosong.
    """
    if len(data) == 0:
        return None

    return min(data)


def cari_suhu_maksimum(data):
    """Mengembalikan suhu tertinggi dari kumpulan suhu.

    Args:
        data (list): Kumpulan suhu yang akan diperiksa.

    Returns:
        int | float | None: Suhu tertinggi, atau None jika data kosong.
    """
    if len(data) == 0:
        return None

    return max(data)


def hitung_rentang(data):
    """Menghitung rentang suhu (suhu maksimum dikurangi suhu minimum).

    Fungsi ini memanfaatkan fungsi lain dalam modul yang sama.

    Args:
        data (list): Kumpulan suhu yang akan dihitung.

    Returns:
        int | float | None: Selisih suhu tertinggi dan terendah,
        atau None jika data kosong.
    """
    if len(data) == 0:
        return None

    return cari_suhu_maksimum(data) - cari_suhu_minimum(data)


def klasifikasi_suhu(suhu):
    """Mengelompokkan suhu ke dalam kategori kenyamanan.

    Aturan kategori:
        >= 33     : Panas
        28-<33    : Hangat
        23-<28    : Nyaman
        < 23      : Sejuk

    Args:
        suhu (int | float): Suhu (derajat Celsius) yang akan diklasifikasikan.

    Returns:
        str: Kategori suhu atau 'Tidak valid' jika di luar rentang -10 sampai 50.
    """
    if suhu < -10 or suhu > 50:
        return "Tidak valid"
    elif suhu >= 33:
        return "Panas"
    elif suhu >= 28:
        return "Hangat"
    elif suhu >= 23:
        return "Nyaman"
    else:
        return "Sejuk"