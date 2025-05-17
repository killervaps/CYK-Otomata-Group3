# Penjelasan Algoritma CYK dan Program

## Penjelasan Mengenai Algoritma CYK dan Cara Kerjanya

Algoritma Cocke-Younger-Kasami (CYK) adalah metode untuk memeriksa apakah sebuah string dapat dihasilkan oleh tata bahasa bebas konteks (context-free grammar) yang telah diubah ke dalam bentuk normal Chomsky (CNF). Dalam CNF, setiap aturan produksi harus berbentuk:
- **A → B C** (A, B, dan C adalah simbol non-terminal), atau
- **A → a** (a adalah simbol terminal).

Algoritma CYK menggunakan pendekatan **bottom-up** dengan membangun tabel dua dimensi yang merepresentasikan semua kemungkinan substring dari string input. Tabel ini diisi secara bertahap untuk menentukan apakah string tersebut sesuai dengan tata bahasa yang diberikan.

### Cara Kerja Algoritma CYK
1. **Inisialisasi Tabel**: 
   - Buat tabel berukuran n x n, di mana n adalah panjang string input.
   - Setiap sel `tabel[i][j]` akan berisi sekumpulan simbol non-terminal yang dapat menghasilkan substring dari posisi i hingga j.

2. **Mengisi Diagonal**:
   - Untuk setiap simbol terminal pada string input (misalnya di posisi i), cari aturan produksi seperti A → a.
   - Masukkan simbol non-terminal (A) ke dalam `tabel[i][i]`.

3. **Mengisi Tabel untuk Substring Lebih Panjang**:
   - Untuk panjang substring dari 2 hingga n:
     - Tentukan posisi awal i dan posisi akhir j.
     - Untuk setiap titik pemisahan k (antara i dan j-1), periksa kombinasi simbol non-terminal di `tabel[i][k]` dan `tabel[k+1][j]`.
     - Jika ada aturan seperti X → Y Z, di mana Y ada di `tabel[i][k]` dan Z ada di `tabel[k+1][j]`, tambahkan X ke `tabel[i][j]`.

4. **Keputusan Akhir**:
   - Jika simbol awal 'S' ada di `tabel[0][n-1]` (sel yang mencakup seluruh string), maka string diterima oleh tata bahasa tersebut. Jika tidak, string ditolak.

---

## Cara Menggunakan Program
1. **Definisikan Tata Bahasa (Grammar)**:
   - Tata bahasa didefinisikan dalam bentuk dictionary Python.
   - Contoh tata bahasa dari kode :
     ```python
     grammar = {
         'S': [['A', 'T']],
         'T': [['B', 'C']],
         'A': [['a']],
         'B': [['b']],
         'C': [['c']]
     }
     ```
     Ini berarti:
     - S → A T
     - T → B C
     - A → a
     - B → b
     - C → c

2. **Siapkan String Input**:
   - String input harus berupa daftar (list) simbol terminal.
   - Contoh:
     ```python
     input_string = ["a", "a", "a", "b", "c"]
     ```

3. **Jalankan Fungsi `cyk_parse`**:
   - Panggil fungsi `cyk_parse(grammar, input_string)` untuk memeriksa apakah string diterima.
   - Fungsi ini mengembalikan `True` jika string diterima dan `False` jika tidak.

4. **Tampilkan Hasil**:
   - Gunakan perintah `print` untuk menampilkan hasil, seperti yang ada di kode :
     ```python
     result = cyk_parse(grammar, input_string)
     print("Accepted by grammar" if result else "Not accepted by grammar")
     ```

---

## Contoh Input dan Output
### String Input
String input: `["a", "a", "a", "b", "c"]` (panjang n = 5)

Tata bahasa yang digunakan:
- S → A T
- T → B C
- A → a
- B → b
- C → c

---

### Langkah 1: Inisialisasi Tabel
Tabel awalnya kosong di semua sel.


|   | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| 0 | {} | {} | {} | {} | {} |
| 1 |    | {} | {} | {} | {} |
| 2 |    |    | {} | {} | {} |
| 3 |    |    |    | {} | {} |
| 4 |    |    |    |    | {} |


---

### Langkah 2: Mengisi Diagonal (Panjang Substring = 1)
Mengisi sel-sel diagonal (i = j) dengan non-terminal yang menghasilkan simbol terminal pada posisi tersebut.

- Pos 0 ("a"): A → a → tabel[0][0] = {'A'}
- Pos 1 ("a"): A → a → tabel[1][1] = {'A'}
- Pos 2 ("a"): A → a → tabel[2][2] = {'A'}
- Pos 3 ("b"): B → b → tabel[3][3] = {'B'}
- Pos 4 ("c"): C → c → tabel[4][4] = {'C'}


|   | 0   | 1   | 2   | 3   | 4   |
|---|---|---|---|---|---|
| 0 | {A} | {}  | {}  | {}  | {}  |
| 1 |     | {A} | {}  | {}  | {}  |
| 2 |     |     | {A} | {}  | {}  |
| 3 |     |     |     | {B} | {}  |
| 4 |     |     |     |     | {C} |


---

### Langkah 3: Mengisi Tabel untuk Panjang 2
Periksa substring berukuran 2 dan kombinasi aturan produksi.

- **i=0, j=1 ("a a")**: 
  - Pemisahan: tabel[0][0] = {'A'}, tabel[1][1] = {'A'} → Tidak ada aturan X → A A → tabel[0][1] = {}
- **i=1, j=2 ("a a")**: 
  - Pemisahan: tabel[1][1] = {'A'}, tabel[2][2] = {'A'} → Tidak ada aturan X → A A → tabel[1][2] = {}
- **i=2, j=3 ("a b")**: 
  - Pemisahan: tabel[2][2] = {'A'}, tabel[3][3] = {'B'} → Tidak ada aturan X → A B → tabel[2][3] = {}
- **i=3, j=4 ("b c")**: 
  - Pemisahan: tabel[3][3] = {'B'}, tabel[4][4] = {'C'} → Aturan T → B C → tabel[3][4] = {'T'}


|   | 0   | 1   | 2   | 3   | 4   |
|---|---|---|---|---|---|
| 0 | {A} | {}  | {}  | {}  | {}  |
| 1 |     | {A} | {}  | {}  | {}  |
| 2 |     |     | {A} | {}  | {}  |
| 3 |     |     |     | {B} | {T} |
| 4 |     |     |     |     | {C} |


---

### Langkah 4: Mengisi Tabel untuk Panjang 3
Periksa substring berukuran 3.

- **i=0, j=2 ("a a a")**: 
  - k=0: tabel[0][0] = {'A'}, tabel[1][2] = {} → kosong
  - k=1: tabel[0][1] = {}, tabel[2][2] = {'A'} → kosong
  - tabel[0][2] = {}
- **i=1, j=3 ("a a b")**: 
  - k=1: tabel[1][1] = {'A'}, tabel[2][3] = {} → kosong
  - k=2: tabel[1][2] = {}, tabel[3][3] = {'B'} → kosong
  - tabel[1][3] = {}
- **i=2, j=4 ("a b c")**: 
  - k=2: tabel[2][2] = {'A'}, tabel[3][4] = {'T'} → Aturan S → A T → tabel[2][4] = {'S'}
  - k=3: tabel[2][3] = {}, tabel[4][4] = {'C'} → kosong


|   | 0   | 1   | 2   | 3   | 4   |
|---|---|---|---|---|---|
| 0 | {A} | {}  | {}  | {}  | {}  |
| 1 |     | {A} | {}  | {}  | {}  |
| 2 |     |     | {A} | {}  | {S} |
| 3 |     |     |     | {B} | {T} |
| 4 |     |     |     |     | {C} |


---

### Langkah 5: Mengisi Tabel untuk Panjang 4
Periksa substring berukuran 4.

- **i=0, j=3 ("a a a b")**: 
  - k=0: tabel[0][0] = {'A'}, tabel[1][3] = {} → kosong
  - k=1: tabel[0][1] = {}, tabel[2][3] = {} → kosong
  - k=2: tabel[0][2] = {}, tabel[3][3] = {'B'} → kosong
  - tabel[0][3] = {}
- **i=1, j=4 ("a a b c")**: 
  - k=1: tabel[1][1] = {'A'}, tabel[2][4] = {'S'} → Tidak ada aturan X → A S → kosong
  - k=2: tabel[1][2] = {}, tabel[3][4] = {'T'} → kosong
  - k=3: tabel[1][3] = {}, tabel[4][4] = {'C'} → kosong
  - tabel[1][4] = {}


|   | 0   | 1   | 2   | 3   | 4   |
|---|---|---|---|---|---|
| 0 | {A} | {}  | {}  | {}  | {}  |
| 1 |     | {A} | {}  | {}  | {}  |
| 2 |     |     | {A} | {}  | {S} |
| 3 |     |     |     | {B} | {T} |
| 4 |     |     |     |     | {C} |


---

### Langkah 6: Mengisi Tabel untuk Panjang 5
Periksa seluruh string "a a a b c".

- **i=0, j=4 ("a a a b c")**: 
  - k=0: tabel[0][0] = {'A'}, tabel[1][4] = {} → kosong
  - k=1: tabel[0][1] = {}, tabel[2][4] = {'S'} → kosong
  - k=2: tabel[0][2] = {}, tabel[3][4] = {'T'} → kosong
  - k=3: tabel[0][3] = {}, tabel[4][4] = {'C'} → kosong
  - tabel[0][4] = {}


|   | 0   | 1   | 2   | 3   | 4   |
|---|---|---|---|---|---|
| 0 | {A} | {}  | {}  | {}  | {}  |
| 1 |     | {A} | {}  | {}  | {}  |
| 2 |     |     | {A} | {}  | {S} |
| 3 |     |     |     | {B} | {T} |
| 4 |     |     |     |     | {C} |


---

### Tabel CYK Akhir
Berikut adalah tabel CYK yang dihasilkan:

|   | 0   | 1   | 2   | 3   | 4   |
|---|---|---|---|---|---|
| **0** | {'A'} | {}    | {}    | {}    | {}    |
| **1** |       | {'A'} | {}    | {}    | {}    |
| **2** |       |       | {'A'} | {}    | {'S'} |
| **3** |       |       |       | {'B'} | {'T'} |
| **4** |       |       |       |       | {'C'} |

### Output
- `tabel[0][4]` (sel yang mencakup seluruh string "a a a b c") kosong dan tidak mengandung 'S'.
- Hasil dari `cyk_parse`: `False`.
- Output program:
  ```
  Not accepted by grammar
  ```
