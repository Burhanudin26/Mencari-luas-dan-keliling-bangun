import math

def main():
    print("\nApa yang anda ingin hitung? Luas atau Keliling (Tulis huruf depan saja)")
    Perintah=input("\n: ").lower().strip()
    if "l" in Perintah:
        luas()
    elif "k" in Perintah:
        keliling()
    else:
        print("Maaf masukkan anda salah")
        main()

def luas():
    masukan_1=input("\nLuas apa yang ingin anda cari: ").lower()
    masukan_1=masukan_1.replace(" ","")

    if "lingkaran" in masukan_1:
        jari_jari=int(input("\nmasukkan nilai jari-jari :"))
        Luas_lingkaran= jari_jari*jari_jari*math.pi
        print("\n luas lingkaran anda adalah: ", Luas_lingkaran, " persegi")

    elif "persegipanjang" in masukan_1:
        panjang=int(input("\nmasukkan nilai panjang: "))
        lebar=int(input("\nmasukkan nilai lebar: "))
        Luas_persegipanjang=panjang*lebar
        print("Luas persegi panjangmu adalah ",Luas_persegipanjang," persegi")

    elif "persegi" in masukan_1:
        sisi=int(input("\nmasukkan nilai panjang sisinya: "))
        Luas_persegi=sisi**2
        print("Luas persegimu adalah ",Luas_persegi," persegi")

    elif "segitiga" in masukan_1:
        panjang=int(input("\nmasukkan nilai panjang: "))
        tinggi=int(input("\nmasukkan nilai lebar: "))
        Luas_segitiga=panjang*tinggi*0.5
        print("Luas segitigamu adalah ",Luas_segitiga," persegi")

    else:
        print("Maaf, tolong ulangi kembali")
        luas()


def keliling():
    masukan_2=input("\nKeliling apa yang ingin anda cari: ").lower()
    masukan_2=masukan_2.replace(" ","")

    if "lingkaran" in masukan_2:
        jari_jari=int(input("\nmasukkan nilai jari-jari :"))
        keliling_lingkaran= jari_jari*math.pi*2
        print("\n keliling lingkaran anda adalah: ", keliling_lingkaran,)

    elif "persegipanjang" in masukan_2:
        panjang=int(input("\nmasukkan nilai panjang: "))
        lebar=int(input("\nmasukkan nilai lebar: "))
        keliling_persegipanjang=panjang*2+lebar*2
        print("keliling persegi panjangmu adalah ",keliling_persegipanjang,)

    elif "persegi" in masukan_2:
        sisi=int(input("\nmasukkan nilai panjang sisinya: "))
        keliling_persegi=sisi*4
        print("keliling persegimu adalah ",keliling_persegi,)

    elif "segitiga" in masukan_2:
        sisi=int(input("\nmasukkan nilai panjang: "))
        keliling_segitiga=sisi*3
        print("keliling segitigamu adalah ",keliling_segitiga,)

    else:
        print("Maaf, tolong ulangi kembali") 
        keliling()

main()
