import os,sys

class hotel():
    def __init__(self,stop=False,rs=5,rd=5,vdd=3,vsr=2):
        self.stop=stop
        self.rs=rs
        self.rd=rd
        self.vdd=vdd
        self.vsr=vsr

    def cls(self):
        if os.name=="nt":
            os.system("cls")
        else:
            os.system("clear")
        print("Hotel Bejjo\n~~~~~~~~~~~")
    def formatrupiah(self,uang):
        y = str(uang)
        if len(y) <= 3 :
            return 'Rp. ' + y
        else :
            p = y[-3:]
            q = y[:-3]
            return self.formatrupiah(q) + ',' + p
    def daftarKamar(self):
        while True:
            try:
                self.cls()
                print("1. Reguler Single\n2. Reguler Double\n3. VIP Double Deluxe\n4. VVIP Super Room")
                print("Catatan : pilih 0 untuk kembali")
                n=int(input("\nMasukkan Pilihan : "))
                if n==1:
                    print("Reguler Single : Tersedia {} Kamar\nHarga : Rp. 300,000/Malam".format(self.rs))
                    input("Enter...")
                elif n==2:
                    print("Reguler Double : Tersedia {} Kamar\nHarga : Rp. 500,000/Malam".format(self.rd))
                    input("Enter...")
                elif n==3:
                    print("VIP Double Deluxe : Tersedia {} Kamar\nHarga : Rp. 800,000/Malam".format(self.vdd))
                    input("Enter...")
                elif n==4:
                    print("VVIP Super Room : Tersedia {} Kamar\nHarga : Rp. 1,000,000/Malam".format(self.vsr))
                    input("Enter...")
                elif n==0:
                    break
            except:
                pass
    def tamuForm(self):
        while True:
            try:
                self.cls()
                print("1. Daftar Kamar\n2. Pemesanan")
                print("Catatan : pilih 0 untuk kembali")
                n=int(input("\nMasukkan Pilihan : "))
                if n==1:
                    self.daftarKamar()
                elif n==2:
                    self.extraPesan()
                elif n==0:
                    break
            except:
                pass
    def extraPesan(self):
        while True:
            try:
                self.cls()
                print("1. Reguler Single\n2. Reguler Double\n3. VIP Double Deluxe\n4. VVIP Super Room")
                print("Catatan : pilih 0 untuk kembali")
                n=int(input("\nMasukkan Pilihan : "))
                if n==1:
                    if self.rs>0:
                        self.calculate(n,"Reguler Single",300000)
                    else:
                        print("Kamar tidak tersedia, hubungi admin untuk lebih lanjut")
                        input("Enter...")
                elif n==2:
                    if self.rd>0:
                        self.calculate(n,"Reguler Double",500000)
                    else:
                        print("Kamar tidak tersedia, hubungi admin untuk lebih lanjut")
                        input("Enter...")
                elif n==3:
                    if self.vdd>0:
                        self.calculate(n,"VIP Double Deluxe",800000)
                    else:
                        print("Kamar tidak tersedia, hubungi admin untuk lebih lanjut")
                        input("Enter...")
                elif n==4:
                    if self.vsr>0:
                        self.calculate(n,"VVIP Super Room",1000000)
                    else:
                        print("Kamar tidak tersedia, hubungi admin untuk lebih lanjut")
                        input("Enter...")
                elif n==0:
                    break
            except:
                pass
    def calculate(self,pilih,kamar,harga):
        hwlong = int(input("{}(Malam) : ".format(kamar)))
        price = hwlong*harga
        total=price
        agree1=""
        agree2=""
        while True:
            try:
                self.cls()
                print("\nData Pemesanan\n--------------")
                print("{} {} x {} Malam = {} [Include]".format(kamar,self.formatrupiah(harga),hwlong,self.formatrupiah(price)))
                print("1. Extra Bed Rp. 100,000 {}".format(agree1))
                print("2. Batal")
                print("3. Bayar")
                print("Total yang harus dibayar : {}".format(self.formatrupiah(total)))
                n=int(input("\nMasukkan Pilihan : "))
                if n==1:
                    if agree1=="":
                        total+=100000
                        agree1="[Include]"
                    else:
                        total-=100000
                        agree1=""
                elif n==2:
                    break
                elif n==3:
                    n=input("Periksa kembali!, Konfirmasi[Y/N] : ").upper()
                    if n=="Y":
                        if pilih==1:
                            self.rs-=1
                        elif pilih==2:
                            self.rd-=1
                        elif pilih==3:
                            self.vdd-=1
                        elif pilih==4:
                            self.vsr-=1
                        print("Terima kasih sudah memilih kami untuk hari anda yang indah")
                        input("Enter...")
                        break
            except:
                pass
    def home(self):
        while True:
            self.cls()
            print("Selamat Datang :)")
            input("Enter...")
            while True:
                try:
                    self.cls()
                    print("1. Masuk\n2. Keluar")
                    print("Catatan : pilih 0 untuk kembali")
                    n=int(input("\nMasukkan Pilihan : "))
                    self.cls()
                    if n==1:
                        while True:
                            try:
                                self.cls()
                                print("1. Menu Utama")
                                print("Catatan : pilih 0 untuk kembali")
                                n=int(input("\nMasukkan Pilihan : "))
                                self.cls()
                                if n==1:
                                    self.tamuForm()
                                elif n==0:
                                    break
                            except:
                                pass
                    elif n==2:
                        self.stop=True
                        sys.exit()#this code to move you in except line(So you can change this line with error sintaks)
                    elif n==0:
                        break
                except:
                    if self.stop==True:
                        sys.exit()

if __name__ == '__main__':
        h = hotel()
        h.home()