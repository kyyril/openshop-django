# OpenShop Django

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-310/)
[![Django Version](https://img.shields.io/badge/django-REST-green.svg)](https://www.djangoproject.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

OpenShop Django adalah layanan RESTful API backend e-commerce yang dibangun menggunakan Django. Proyek ini berfokus pada manajemen produk serta penerapan prinsip HATEOAS (Hypermedia As The Engine Of Application State) untuk memastikan navigasi API yang dinamis dan terstandarisasi.

---

## Daftar Isi

* [Tentang Proyek](#tentang-proyek)
* [Fitur Utama](#fitur-utama)
* [Tech Stack](#tech-stack)
* [Struktur Direktori](#struktur-direktori)
* [Persiapan Instalasi](#persiapan-instalasi)
* [Menjalankan Aplikasi](#menjalankan-aplikasi)
* [Dokumentasi API dan Pengujian](#dokumentasi-api-dan-pengujian)
* [Kontribusi](#kontribusi)
* [Lisensi](#lisensi)

---

## Tentang Proyek

Layanan ini dirancang untuk menyediakan fondasi backend e-commerce yang bersih dan modular. Dengan mengimplementasikan pendekatan HATEOAS, klien yang mengonsumsi API ini dapat menavigasi resource terkait secara dinamis melalui tautan hypermedia yang disertakan langsung di dalam respons payload, mengurangi ketergantungan klien pada hardcode URL endpoint.

---

## Fitur Utama

* **Manajemen Produk**: Operasi dasar CRUD (Create, Read, Update, Delete) untuk pengelolaan data produk e-commerce.
* **Dukungan HATEOAS**: Setiap respons API menyertakan tautan relasional agar klien dapat mengetahui aksi selanjutnya yang tersedia.
* **Koleksi Pengujian API**: Menyediakan file konfigurasi lingkungan dan koleksi pengujian siap pakai untuk mempermudah validasi endpoint.

---

## Tech Stack

* **Bahasa Pemrograman**: Python 3.10
* **Framework**: Django
* **Database**: SQLite (Default untuk pengembangan lokal)
* **Manajemen Dependensi**: Pipenv / Pip

---

## Struktur Direktori

Struktur direktori proyek disusun sebagai berikut:

```text
openshop-django/
├── openshop/                              # Konfigurasi dan pengaturan utama proyek Django
├── products/                              # Aplikasi inti untuk manajemen produk dan endpoint HATEOAS
├── OpenShopAPITestCollectionAndEnvironment/ # Koleksi pengujian API dan environment
├── Pipfile                                # Definisi dependensi menggunakan Pipenv
├── Pipfile.lock                           # Lockfile dependensi Pipenv
├── requirements.txt                       # Daftar dependensi flat
├── db.sqlite3                             # Database SQLite pengembangan
└── manage.py                              # Utilitas command-line Django
