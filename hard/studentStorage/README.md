#Ivan Christopher Yaprianto
#C14190193

Disini merupakan arsitektur student paper storage berbasiskan REST yang memiliki 6 servis, yaitu

Login: 'POST', 'localhost:8000/api/login'
Melakukan login dan session dimulai serta terisi sesuai dengan id student yang login

Logout: 'GET', 'localhost:8000/logout'
Melakukan logout dan session pun berakhir

Register: 'POST', 'localhost:8000/api/register'
Melakukan penambahan data student yang belum pernah terdaftar dan ingin melakukan login tapi belum bisa

Upload File: 'POST', 'localhost:8000/upload'
Untuk upload file ke database dan akan terdaftar sesuai dengan id student yang melakukan upload

Download File: 'GET', 'localhost:8000/download'
Untuk melakukan download file dari database dan hanya bisa dilakukan jika id student yang memiliki hak akses yang merequest download

Search: 'GET', 'localhost:9200/search/title'
Menggunakan elasticsearch untuk melakukan pencarian title yang di request dan memberi output file yang mengandung title tersebut dari database
