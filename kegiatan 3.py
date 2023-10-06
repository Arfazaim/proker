class Orang:
#variabel class, untuk menghitung jumlah orang
    total=0
    def __init__ (self, nama):
# inisiasi data, data yang dibuat pada self merupakan variabel obyek
        self.nama = nama 
#ketika ada orang yang dibuat, tambahkan total orang Orang.total +
        Orang.total += 1
        
        
    def __del__(self):
#kurangi total orang jika objek dihapus Orang.total -=1 
        Orang.total -=1
        
    def katakanHalo (self):
        print ("Halo, nama saya", self.nama, ", apa kabar?") 
    def total_populasi (Orang): 
        print ('Total Orang adalah, Orang. total')
        
# method class
total_populasi = classmethod
org=Orang ('budi')
org.katakanHalo ()
print ("Total orang ", Orang.total)

org2=Orang ('andi')
org2.katakanHalo () 
print ("Total orang ", Orang.total)

print ('objek dihapus')
del org
del org2
print ("Total orang yang dihapus adalah", Orang.total)