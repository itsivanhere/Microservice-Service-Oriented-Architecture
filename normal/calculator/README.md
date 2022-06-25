#Ivan Christopher Yaprianto
#C14190193

Ini merupakan arsitektur Simple calculator service yang menggunakan Celery dan Flask untuk melakukan task perhitungan. Terdapat 2 request yang bisa dilakukan yaitu;
*Note: untuk menjalankan celery, masukkan command sebagai berikut: celery -A main_celery  worker -l info -P eventlet

Output angka prima pada index request: 'GET', 'localhost:5000/api/prime/<index>'

Output angka prima palindormm pada index request: 'GET', 'localhost:5000/api/prime/palindrome/<index>'