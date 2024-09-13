import streamlit as st
import pandas as pd

#import library visualisasi
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def run():
    #buat judul 
    st.title('Cardiovascular Classification Disease Identification')
    st.write('### Membantu Anda Mengenali Risiko Kardiovaskular Secara Cepat dan Efisien')

    #import gambar lewat url -> copy image address
    st.image('https://assets.suitdev.com/emc-assets/files/CoE/cardiovaskular%20center.jpg')

    #nambahin subheader
    st.subheader('Data Information: ')

    #tambahin dataframe
    data = pd.read_csv('cardio_train.csv', sep=';')
    st.dataframe(data)

    ############################
    #visualisasi
    st.write('### 1. Distribusi Indikasi:')
    # Hitung jumlah kemunculan setiap nilai di kolom 'cardio'
    class_counts = data['cardio'].value_counts()

    # Tentukan label untuk setiap nilai
    labels = ['Terindikasi Cardiovascular', 'Tidak Terindikasi Cardiovascular']

    # Tentukan warna untuk setiap nilai
    colors = ['darkorange', 'blue']

    # Buat pie plot
    fig, ax = plt.subplots()
    ax.pie(class_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)

    # Tambahkan judul
    ax.set_title('Distribusi Indikasi')

    # Equal aspect ratio ensures that pie is drawn as a circle
    ax.axis('equal')

    # Tampilkan plot di Streamlit
    st.pyplot(fig)
    st.write('- Dari hasil visualisasi diatas, didapatkan  bahwa pada kolom target ini nantinya balance. Karena yang terindikasi dan yang tidak terindikasi hasilnya 50:50.\n'
             '\n')

    ################################################################
    st.write('### 2. Distribusi Indikasi Berdasarkan Jenis Kelamin:')
    # Menghitung jumlah kejadian dari setiap nilai pada kolom 'cardio' berdasarkan jenis kelamin
    class_counts_by_gender = data.groupby('gender')['cardio'].value_counts().unstack()

    # Mendefinisikan warna untuk setiap nilai cardiovascular
    colors = ['darkorange', 'blue']

    # Membuat diagram batang
    fig, ax = plt.subplots()
    class_counts_by_gender.plot(kind='bar', color=colors, ax=ax)

    # Menambahkan label sumbu x
    ax.set_xlabel('Jenis Kelamin')

    # Menambahkan label sumbu y
    ax.set_ylabel('Jumlah Kasus')

    # Menambahkan judul
    ax.set_title('Distribusi Indikasi Cardiovascular Berdasarkan Jenis Kelamin')

    # Menambahkan legend
    ax.legend(['Tidak Terindikasi Cardiovascular', 'Terindikasi Cardiovascular'], loc='upper right')

    # Mengubah label x-axis dengan nama gender yang lebih deskriptif
    ax.set_xticks(range(len(class_counts_by_gender.index)))
    ax.set_xticklabels(class_counts_by_gender.index, rotation='horizontal')

    # Menampilkan jumlah kasus di atas setiap batang
    for container in ax.containers:
        ax.bar_label(container, label_type='edge')

    # Menampilkan plot di Streamlit
    st.pyplot(fig)
    st.write('- Dari perbandingan visualisasi diatas, dapat dilihat bahwa jumlah yang terindikasi kebanyakan adalah dari gender perempuan, dengan jumlah pasien yang terindikasi sebesar 22.379, dan untuk laki-laki sebesar 12.243.')


    ################################################################
    st.write('### 3. Indikasi Perbandingan berdasarkan rata-rata :')
    # Menghitung deskripsi untuk pasien yang terindikasi dan tidak terindikasi kardiovaskular
    cardio = data[data['cardio'] == 1].describe().T
    no_cardio = data[data['cardio'] == 0].describe().T

    # Mendefinisikan warna untuk heatmap
    colors = ['blue', 'darkorange']

    # Membuat figure dan axis untuk heatmap
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

    # Heatmap untuk pasien yang terindikasi
    sns.heatmap(cardio[['mean']], annot=True, cmap=colors, linewidths=0.4, linecolor='white', cbar=False, fmt='.2f', ax=ax[0])
    ax[0].set_title('Cardio Disease')

    # Heatmap untuk pasien yang tidak terindikasi
    sns.heatmap(no_cardio[['mean']], annot=True, cmap=colors, linewidths=0.4, linecolor='white', cbar=False, fmt='.2f', ax=ax[1])
    ax[1].set_title('No Cardio Disease')

    # Mengatur tata letak untuk memastikan plot tidak saling bertumpuk
    fig.tight_layout(pad=0.5)

    # Tampilkan plot di Streamlit
    st.pyplot(fig)
    st.write(' - Rata-rata usia yang terkena cardiovascular adalah 54,9 tahun, sedangkan yang tidak 51,7 tahun.\n'
    ' - Rata-rata Kadar ap_hi dan ap_lo juga berpengaruh untuk orang yang terindikasi cardiovascular, dapat dilihat yang terindikasi memiliki rata-rata yang lebih tinggi daripada yang tidak.\n'  

    ' - Kadar glukosa dalam tubuh pada pasien yang terindikasi lebih tinggi daripada yang tidak terindikasi.\n'  

    ' - Aktifitas fisik terlihat bahwa rata-rata pasien yang tidak terindikasi memiliki aktifitas fisik yang lebih tinggi daripada yang terindikasi.\n')

    ################################################################
    st.write('### 4. Korelasi setiap kolom :')
    # Menghitung matriks korelasi
    correlation_matrix = data.corr()

    # Membuat figure dan axis untuk heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")

    # Menambahkan judul
    plt.title('Correlation Heatmap of Numerical Columns')

    # Menampilkan plot di Streamlit
    st.pyplot(plt.gcf())
    st.write('Berdasarkan visualisasi diatas dapat diasumsikan bahwa: \n'
    ' - Variabel yang memiliki korelasi positif cukup kuat adalah ap_hi (tekanan darah sistolik) dan ap_lo (tekanan darah diastolik), dengan nilai korelasi sekitar 0.45. Hal ini menunjukkan bahwa ketika tekanan darah sistolik meningkat, tekanan darah diastolik juga cenderung meningkat.\n' 

    ' - Ada korelasi moderat antara age (usia) dan cholesterol dengan nilai korelasi sekitar 0.22, yang menunjukkan bahwa seiring bertambahnya usia, kadar kolesterol cenderung meningkat.\n'  

    ' - Korelasi positif moderat lainnya adalah antara age dan cardio (sekitar 0.24), menunjukkan bahwa risiko penyakit kardiovaskular cenderung meningkat seiring bertambahnya usia.\n' 

    ' - Hubungan Lemah atau Tidak Ada Hubungan:  sebagian besar variabel lainnya memiliki korelasi yang sangat lemah atau mendekati nol, seperti gender dengan variabel lain, atau smoke dengan cardio. Ini menunjukkan bahwa tidak ada hubungan linear yang signifikan di antara variabel-variabel ini.\n' 

    ' - Beberapa variabel memiliki korelasi negatif yang lemah, misalnya smoke dengan height (-0.05) atau active dengan cardio (-0.04).\n')

    ################################
    st.write("### 5. Cardiovascular Disease Distribution by Smoking Status")
    # Warna untuk plot
    colors = ['darkorange', 'blue']

    # Membuat plot menggunakan seaborn
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x='smoke', hue='cardio', palette=colors)

    # Menambahkan judul dan label
    plt.title('Cardiovascular Disease Distribution by Smoking Status')
    plt.xlabel('Smoking Status (1 = Smoker, 0 = Non-Smoker)')
    plt.ylabel('Count')
    plt.legend(title='Cardio', labels=['No Disease', 'Has Disease'])

    # Menampilkan plot di Streamlit
   
    st.pyplot(plt.gcf())
    st.write('- Ternyata berdasarkan dataset, orang yang cenderung merokok lebih sedekat terkena cardiovascular desease, berarti merokok bukanlah faktor utama penyebab cardiovascular.')

    ################################
    st.write('### 6. Cardiovascular Disease Distribution by Cholesterol Status: ')
    # Membuat plot menggunakan seaborn
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x='cholesterol', hue='cardio', palette=colors)

    # Menambahkan judul dan label
    plt.title('Cardiovascular Disease Distribution by Cholesterol Status')
    plt.xlabel('Kategori kadar kolesterol pasien (1: normal, 2: di atas normal, 3: jauh di atas normal).  ')
    plt.ylabel('Count')
    plt.legend(title='Cardio', labels=['No Disease', 'Has Disease'])

    st.pyplot(plt.gcf())
    st.write('- Terlihat bahwa pasien dengan kadar kolesterol yang lebih tinggi (kategori 2 dan 3) cenderung memiliki angka penyakit kardiovaskular yang lebih tinggi. Kadar kolesterol yang tinggi sering dikaitkan dengan risiko penyakit jantung.')


    ######################
    st.write('### 7. Cardiovascular Disease Distribution by Cholesterol Status: ')
    # Membuat plot menggunakan seaborn
    plt.figure(figsize=(8, 6))
    sns.countplot(data=data, x='gluc', hue='cardio', palette=colors)

    # Menambahkan judul dan label
    plt.title('Cardiovascular Disease Distribution by Cholesterol Status')
    plt.xlabel('Kategori kadar glukosa pasien (1: normal, 2: di atas normal, 3: jauh di atas normal).')
    plt.ylabel('Count')
    plt.legend(title='Cardio', labels=['No Disease', 'Has Disease'])

    st.pyplot(plt.gcf())
    st.write('- Dari dataset tersebut, saya berasumsi distribusi tidak make sense. Banyak pasien dengan kadar glukosa normal (kategori 1) juga memiliki penyakit kardiovaskular. Ini tampak tidak sesuai dengan kenyataan, tetapi bisa jadi ada faktor lain yang lebih dominan mempengaruhi risiko ini, seperti tekanan darah atau obesitas.')