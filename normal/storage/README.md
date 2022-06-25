#Ivan Christopher Yaprianto
#C14190193

Disini merupakan arsitektur Simple cloud storage berbasiskan REST yang memiliki 6 servis, yaitu

Upload File: 'POST', 'localhost:8000/upload'
Untuk upload file ke database dan akan terdaftar sesuai dengan id student yang melakukan upload

Download File: 'GET', 'localhost:8000/download'
Untuk melakukan download file dari database dan hanya bisa dilakukan jika id student yang memiliki hak akses yang merequest download
