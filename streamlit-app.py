import streamlit as st
import pickle
import base64
import numpy as np
import pandas as pd

kanker_model = pickle.load(open('./stream_model/ipyd_model.sav', 'rb'))


def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# back ground
def set_png_as_page_bg(png_file):
    try:
        bin_str = get_base64_of_bin_file(png_file)
        page_bg_img = '''
        <style>
        .stApp {
            background-image: url("data:image/png;base64,%s");
            background-size: cover;
        }
        </style>
        ''' % bin_str
        
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except Exception as e:
        print("Error:", e)

set_png_as_page_bg('stream_model/img/inidia.png')

st.header(':red[Breast Cancer] Classification :medical_symbol:', divider='rainbow')

col1, col2 = st.columns(2)
# kolom 1
with col1:
    x_radius_mean = st.text_input('mean radius')
    x_texture_mean = st.text_input('mean texture')
    x_perimeter_mean = st.text_input('mean perimeter')
    x_area_mean = st.text_input('mean area')
    x_smoothness_mean = st.text_input('mean smooothness')
    x_compactness_mean = st.text_input('mean compactness')
    x_concavity_mean = st.text_input('mean concavity')
    x_concave_pts_mean = st.text_input('mean number of concave portions of the contour')
    x_symmetry_mean = st.text_input('mean symmetry')
    x_radius_se = st.text_input('standard error of the radius')
    x_parimeter_se = st.text_input('standard error of the perimeter')
    x_area_se = st.text_input('standard error of the area')
    x_concave_pts_se = st.text_input('standard error of the number of concave portions of the contour')
# kolom 2
with col2:
    x_compactness_se = st.text_input('standard error of the compactness')
    x_concavity_se = st.text_input('standard error of the concavity')
    x_fractal_dim_se = st.text_input('standard error of the "coastline approximation"')
    x_radius_worst = st.text_input('worst (largest) radius')
    x_texture_worst = st.text_input('worst (most severe) texture')
    x_perimeter_worst = st.text_input('worst (largest) perimeter')
    x_area_worst = st.text_input('worst (largest) area')
    x_smoothness_worst = st.text_input('worst (most severe) smoothness')
    x_compactness_worst = st.text_input('worst (most severe) compactness')
    x_concavity_worst = st.text_input('worst (most severe) concavity')
    x_symmetry_worst = st.text_input('worst (most severe) symmetry')
    x_fractal_dim_worst = st.text_input('worst (most severe) "coastline approximation"')
    x_concave_pts_worst = st.text_input('worst (most severe) number of concave portions of the contour')


new_data = [[x_radius_mean, x_texture_mean, x_perimeter_mean, x_area_mean, x_smoothness_mean, x_compactness_mean,
                     x_concavity_mean, x_concave_pts_mean, x_symmetry_mean, x_radius_se, x_parimeter_se, x_area_se,
                     x_compactness_se, x_concavity_se, x_concave_pts_se, x_fractal_dim_se, x_radius_worst, x_texture_worst,
                     x_perimeter_worst, x_area_worst, x_smoothness_worst, x_compactness_worst, x_concavity_worst, x_concave_pts_worst,
                     x_symmetry_worst, x_fractal_dim_worst
                     ]]

if st.button('Classifcation The Cancer'):
    print(new_data)
    try:
        patient_class = kanker_model.predict(new_data)

        if patient_class[0] == 'M':
            patient_diag = 'The cancers category is Malignant'
        else:
            patient_diag = 'The cancers category is Benign'

        st.success(patient_diag)
    except:
        e = RuntimeError('Please input data correctly')
        st.exception(e)