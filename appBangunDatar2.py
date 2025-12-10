import streamlit as st

# halaman utama
st.title('aplikasi perhitungan luas bangun datar')
st.header('ini buatan anak SI')

menu = st.sidebar.selectbox('pilih aplikasi', ['luas persegi', 'luas segitiga', 'luas lingkaran'])

if menu == 'luas persegi':
    st.write('ini halan untuk menghitung luas persegi')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi.jpg', caption='gambar persegi')
    def luaspersegi(a):
        return a*a
    sisi = st.number_input('silahkan masukan sisi', min_value=0,)

    if st.button('hitung'):
        luas = luaspersegi(sisi)
        st.success(f'luas persegi adalah {luas}')

elif menu == 'luas segitiga':
    st.write('ini halan untuk menghitung luas segitiga')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/06/rumus-luas-segitiga-sama-sisi.jpg', caption='gambar segitiga')
    def luassegitiga(a, t):
        return 0.5*a*t
    alas = st.number_input('silahkan masukan alas', min_value=0,)
    tinggi = st.number_input('silahkan masukan tinggi', min_value=0, )

    if st.button('hitung'):
        luas = luassegitiga(alas, tinggi)
        st.success(f'luas segitiga adalah {luas}')

elif menu == 'luas lingkaran':
    st.write('ini halaman untuk menghitung luas lingkaran')
    st.image('https://cdn.law-justice.co/posts/1/2021/2021-12-07/052c78ccf3d558b1f738bb09d5ec6090_1.jpg', caption='gambar lingkaran')
    def luaslingkaran(r):
        return 3.14*r*r
    radius = st.number_input('silahkan masukan jari-jari', min_value=0, )

    if st.button('hitung'):
        luas = luaslingkaran(radius)
        st.success(f'luas lingkaran adalah {luas}')

elif menu == 'luas persegi panjang':
    st.write('ini halaman untuk menghitung luas lingkaran')
    st.image('https://www.doyanblog.com/wp-content/uploads/2023/05/rumus-luas-persegi-panjang.jpg.webp', caption='gambar persegi panjang')
    def luaspersegipanjang(p,l):
        return p*l
    panjang = st.number_input('silahkan masukan panjang', min_value=0,)
    lebar = st.number_input('silahkan masukan lebar', min_value=0)

    if st.button('hitung'):
        luas = luaspersegipanjang(panjang, lebar)
        st.success(f'luas persegi panjang adalah {luas}')

    
