import json, requests, os, Menu

#superclass dari class subGunungApi
class superGunungApi:
  gunung = requests.get("https://indonesia-public-static-api.vercel.app/api/volcanoes")
  gunungSukses = gunung.json()
  #menu 1, tampilkan data---------------------------------------------#
  def show(self): 
    nomor = 0
    for i in self.gunungSukses:
      nomor = nomor+1
      #tampilan
      print("""
      {5}. Gunung {0}
      Bentuk                     : {1}
      Tinggi                     : {2}
      Estimasi letusan terakhir  : {3}
      Geolokasi                  : {4}
      """.format(i["nama"],i['bentuk'],i['tinggi_meter'],i['estimasi_letusan_terakhir'],i['geolokasi'],nomor))
    jeda = input("Tekan enter untuk melanjutkan")
    Menu.menu()
  #menu 2, cari data bedasarkan nama gunung---------------------------#
  def search(self): 
    namaGunung = input("Masukan Pilihan Nama Gunung : ")
    kondisi = False
    gung = superGunungApi()
    #-----------------------------------------------------------------#
    def pilihan2():
      jeda = input("Apakah anda ingin kembali ke menu utama? (y/n)")
      if jeda == 'y':
        Menu.menu()
      elif jeda == 'n':
        gung.search()
        print()
      else:
        pilihan2()
    #-----------------------------------------------------------------#
    def pilihan():     
      jeda = input("Apakah anda ingin mengeprint data ini? (y/n)")
      if jeda == 'y':
        bikinFile = open("Print_data_gunung_api.txt","a")
        bikinFile.write("""
        Nama Gunung               : {0}
        Bentuk Gunung             : {1}
        Tinggi Gunung             : {2}
        Estimasi Letusan Terakhir : {3}
        Geolokasi                 : {4}
        """.format(i["nama"],i["bentuk"],i["tinggi_meter"],i["estimasi_letusan_terakhir"],i["geolokasi"]))
        print("File berhasil di print!")
        jeda = input()
      elif jeda == 'n':
        print()
        print("Anda telah memilih untuk tidak mengeprint data")
      else:
        print()
        print("Input yang anda masukan salah!")
        pilihan()
    #-----------------------------------------------------------------#
    for i in self.gunungSukses:
      if i["nama"] == namaGunung.title():
        kondisi = True
        print("""
        Nama Gunung               : {0}
        Bentuk Gunung             : {1}
        Tinggi Gunung             : {2}
        Estimasi Letusan Terakhir : {3}
        Geolokasi                 : {4}
        """.format(i["nama"],i["bentuk"],i["tinggi_meter"],i["estimasi_letusan_terakhir"],i["geolokasi"]))
        pilihan()
    if kondisi == False:
      print()
      print("Data tidak ditemukan!")
      gung.search()
    #-----------------------------------------------------------------#
    pilihan2()
    Menu.menu()

#subclass dari class superGunungApi
class subGunungApi(superGunungApi):
  #konstruktor
  def __init__(self,pilih):
    self.pilih = pilih
  #menu 3, memfilter data
  def filter(self): 
    #memfilter bedasarkan bentuk
    if self.pilih == 1:
      #-----------------------------------------------------------------# 
      def pilihan():
        jeda = input("Apakah anda ingin kembali ke menu utama? (y/n)")
        if jeda == 'y':
          Menu.menu()
        elif jeda == 'n':
          geng = subGunungApi(1)
          geng.filter()
        else:
          print("Invalid Input")
          jeda = input("Tekan \"Enter\" untuk melanjutkan")
          pilihan()
      #-----------------------------------------------------------------#
      kondisi = False
      inp = input("Masukan bentuk : ")
      nomor = 0
      for i in self.gunungSukses:
        if i["bentuk"] == inp.lower() or i["bentuk"] == inp.title():
          nomor = nomor + 1
          kondisi = True
          print("""
          {0}. {1}""".format(nomor,i["nama"]))
      if kondisi == False:
        print("Invalid Input")
        geng = subGunungApi(1)
        geng.filter()
      pilihan()
      #-----------------------------------------------------------------#
    #memfilter bedasarkan tinggi
    elif self.pilih == 2:
      #-----------------------------------------------------------------#
      def pilihan():
        jeda = input("Apakah anda ingin kembali ke menu utama? (y/n)")
        if jeda == 'y':
          Menu.menu()
        elif jeda == 'n':
          geng = subGunungApi(2)
          geng.filter()
        else:
          print("Invalid Input")
          jeda = input("Tekan \"Enter\" untuk melanjutkan")
          pilihan()
      #-----------------------------------------------------------------#
      kondisi = False
      inp = eval(input("Masukan tinggi : "))
      tinggiGunung = []
      nomor = 0
      #-----------------------------------------------------------------#
      for i in self.gunungSukses:
        tinggiGunung = i["tinggi_meter"]
        if tinggiGunung == "N/A":
          tinggiGunung = int(tinggiGunung.replace("N/A","0"))
        else:
          tinggiGunung = tinggiGunung.replace("−","-")
          tinggiGunung = int(tinggiGunung.replace("meter",""))
        if tinggiGunung > inp:
          kondisi = True
          nomor = nomor + 1
          print("""
          {0}. Gunung {1} 
          dengan tinggi {2}""".format(nomor,i["nama"],i["tinggi_meter"]))
      if kondisi == False:
        print("Data yang anda cari tidak ada")
      pilihan()
    else:
      print("Invalid Input")
    jeda = input("Tekan \"Enter\" untuk melanjutkan")
    Menu.menu()