import streamlit as st
import pandas as pd
import pickle 

# menggunakan streamlit untuk membuat input data
def run():
    # Mapping values to descriptive labels
    cholesterol_mapping = {
        'Normal': 1,
        'Di atas normal': 2,
        'Jauh di atas normal': 3
    }

    gluc_mapping = {
        'Normal': 1,
        'Di atas normal': 2,
        'Jauh di atas normal': 3
    }

    binary_mapping = {
        'Tidak': 0,
        'Ya': 1
    }

    st.title('Prediksi Risiko Kardiovaskular Secara Cepat dan Efisien')

    # load model yang udah dibuat
    with open('best_model.pkl', 'rb') as file_1:
        model = pickle.load(file_1)

    # membuat form untuk input data
    st.write('## Input Data')
    #form input data
    with st.form(key='player'):
        id = st.text_input('id')
        age = st.number_input('age', min_value=10, max_value=10000)
        gender = st.selectbox('Gender', ['1', '2'])
        height = st.number_input('Height', min_value=10, max_value=200)
        weight = st.number_input('Weight', min_value=1, max_value=300)
        ap_hi = st.number_input('Systolic Blood Pressure (ap_hi)', min_value=10, max_value=300)
        ap_lo = st.number_input('Diastolic Blood Pressure (ap_lo)', min_value=10, max_value=300)

        # Menggunakan mapping untuk cholesterol dan gluc
        cholesterol_label = st.selectbox('Kadar Kolesterol', list(cholesterol_mapping.keys()))
        cholesterol_value = cholesterol_mapping[cholesterol_label]

        gluc_label = st.selectbox('Kadar Glukosa', list(gluc_mapping.keys()))
        gluc_value = gluc_mapping[gluc_label]

        # Menggunakan mapping untuk binary options
        smoke_label = st.selectbox('Merokok?', list(binary_mapping.keys()))
        smoke_value = binary_mapping[smoke_label]

        alco_label = st.selectbox('Konsumsi Alkohol?', list(binary_mapping.keys()))
        alco_value = binary_mapping[alco_label]

        active_label = st.selectbox('Aktif secara fisik?', list(binary_mapping.keys()))
        active_value = binary_mapping[active_label]

        cardio_label = st.selectbox('Penyakit Kardiovaskular?', list(binary_mapping.keys()))
        cardio_value = binary_mapping[cardio_label]

        # submit button
        submit = st.form_submit_button(label='Predict')

    if submit:
        data = {
            'id': id,
            'age': age,
            'gender': gender,
            'height': height,
            'weight': weight,
            'ap_hi': ap_hi,
            'ap_lo': ap_lo,
            'cholesterol': cholesterol_value,  # menggunakan nilai numerik
            'gluc': gluc_value,  # menggunakan nilai numerik
            'smoke': smoke_value,  # menggunakan nilai numerik
            'alco': alco_value,  # menggunakan nilai numerik
            'active': active_value,  # menggunakan nilai numerik
            'cardio': cardio_value  # menggunakan nilai numerik
        }

        df = pd.DataFrame([data])
        st.dataframe(df)

        # menyimpan hasil prediksi
        prediction = model.predict(df)
        st.write('# Halo, berdasarkan data yang Anda input, hasil prediksi menunjukkan bahwa Anda:')
        if prediction[0] == 1:
            st.write('## Terindikasi Cardiovascular, silahkan berikan penanganan lebih lanjut kepada pasien!')
        else:
            st.write('## Tidak Terindikasi Cardiovascular')
