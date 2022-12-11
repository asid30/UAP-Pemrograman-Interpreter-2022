import Menu

while(True): #kode ini akan di looping berkali-kali
  try : #try akan menginterpretasikan menu utama sampai terjadi error
    Menu.menu() #memanggil menu utama
  except (NameError,SyntaxError,TypeError): #kode dibawah akan dijalankan ketika terjadi error
    print("Invalid Input")
    print("Tekan \"Enter\" untuk melanjutkan")
    jeda = input()