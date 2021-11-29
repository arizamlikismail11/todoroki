A=[1,2,3,"bintang","cinta","hati"]
print(A)
print()
#tampilkan elemen ke 3
print("elemen ketiga=> ",A[3])
print(A)
print("elemen ke 2 s/d 4 => ",A[2:4])
print(A)
print("elemen terakhir=> ",A[-1])
print(A)
print("=====perubahan elemen====")
print("mengubah cinta jadi benci")
A[4]="benci"
print(A)
#ubah elemen ke 4 sampai dengan elemen terakhir
A[4],A[5]="sayang","jantung"
print("perubahan elemen 4-akhir=> ",A)
print(A)
print()
A.extend([3,4,5])
B=["jeruk","apel","melon"]
B.append([1000,2000,3000])
element=A+B
print("gabungan elemen A dan B")
print(element)