# SISTEM PEMINJAMAN BUKU PERPUSTAKAAN
Aplikasi Sistem Peminjaman Buku Perpustakaan ini adalah tugas dari mata kuliah OOP, penulisan kode program menggunakan cara association antara dua kelas utama yaitu Book (Buku) dan LibraryMember (Anggota Perpustakaan). Setiap objek LibraryMember akan terkait dengan beberapa objek Book yang merupakan daftar buku yang dipinjam oleh anggota tersebut.

## Penjelasan Program
#### Pembuatan Class Book :
Class Book memiliki beberapa atribut, yaitu self.title (untuk input judul buku), self.author (untuk input author buku), self.ada (untuk kondisi buku ada atau tidak).
```sh
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.ada = True
```
#### Pembuatan Class LibraryMember:
Class LibraryMember memiliki beberapa atribut dan method untuk melakukan proses peminjaman dan pengembalian buku, serta menampilkan daftar buku.
```sh
class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.pinjam = []
```
##### method borrow_book
untuk melakukan proses peminjaman buku, sistem akan mengambil data buku yang ingin dipinjam dari Class Book melalui atribut self.pinjam
```sh
def borrow_book(self, book):
        if book.ada:
            book.ada = False
            self.pinjam.append(book)
            print(f"{self.name} berhasil meminjam buku: {book.title}")
        else:
            print(f"Maaf, buku {book.title} sedang dipinjam.")
```
##### method return_book
method untuk melakukan pengembalian buku apabila ada buku yang dipinjam
```sh
def return_book(self, book):
        if book in self.pinjam:
            book.ada = True
            self.pinjam.remove(book)
            print(f"{self.name} berhasil mengembalikan buku: {book.title}")
        else:
            print(f"Maaf, buku {book.title} tidak ada dalam daftar buku yang dipinjam.")
```
##### method display_borrowed_books
untuk menampilkan daftar buku yang sedang dipinjam, menggunakan fungsi len(self.pinjam) untuk memeriksa adakah buku yang sedang dipinjam.
menggunakan for loop untuk menampilkan daftar buku yang dipinjam.

```sh
def display_borrowed_books(self):
        print(f"Daftar Buku yang Dipinjam oleh {self.name}:")
        if len(self.pinjam) == 0:
            print("Tidak ada buku yang dipinjam.")
        else:
            for book in self.pinjam:
                print(f"Judul: {book.title}")
                print(f"Penulis: {book.author}")
                print(f"Status Ketersediaan: {'Tersedia' if book.ada else 'Dipinjam'}")
                print("")
```

##### membuat objek member
```sh
member = LibraryMember(input("Masukkan nama anggota perpustakaan: "))
```

##### membuat sistem input
menggunakan for loop untuk melakukan input data dan mentarnsfer ke Class Book
```sh
n = int(input("Berapa banyak buku yang ingin dipinjam? "))

for i in range(n):
    print(f"\nBuku ke-{i+1}:")
    title = input("Judul: ")
    author = input("Penulis: ")

    book = Book(title, author)
    member.borrow_book(book)
```
menampilkan buku yang dipinjam
```sh
member.display_borrowed_books()
```
##### input pengembalian buku
input data untuk melakukan pengembalian buku
```sh
n = int(input("Berapa banyak buku yang ingin dikembalikan? "))

for i in range(n):
    print(f"\nBuku ke-{i+1}:")
    title = input("Judul: ")
    author = input("Penulis: ")

    book = Book(title, author)
    member.return_book(book)

```
menampilkan daftar buku yang dipinjam setelah pengembalian
```sh
member.display_borrowed_books()
```
