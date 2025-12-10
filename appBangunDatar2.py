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
    