import os
import PkgGunungAPI

#menu utama
def menu(): 
  gung = PkgGunungAPI.superGunungApi.superGunungApi() #deklarasi nama object dari class gunungApi
  os.system('cls') #menghapus layar
  #tampilan menu utama
  print("Menu Utama") 
  print("1. Menampilkan Data")
  print("2. Search")
  print("3. Filter")
  print("9. Exit")
  pilih = eval(input("Masukan Pilihan : "))
  #percabangan menu utama
  if (pilih == 1):
    gung.show()
  elif (pilih == 2):
    gung.search()
  elif (pilih == 3):
    print("1. Bentuk")
    print("2. Tinggi")
    pilih = eval(input("Masukan Pilihan : "))
    gong = PkgGunungAPI.superGunungApi.subGunungApi(pilih)
    gong.filter()
  elif (pilih == 9):
    print("Keluar Program")
    exit()
  else:
    print("Invalid Input")
    jeda = input("Tekan \"Enter\" untuk melanjutkan")