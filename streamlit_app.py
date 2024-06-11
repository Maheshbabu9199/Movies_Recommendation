import streamlit as st
import base64
from src.pipelines.recommendations_pipeline import RecommendationsPipeline




st.title(':rainbow[Movies Recommendations for you..!!]', )

try:
    def get_base64(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    def set_background(png_file):
        bin_str = get_base64(png_file)
        page_bg_img = '''
        <style>
        .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
        }
        </style>
        ''' % bin_str
        st.markdown(page_bg_img, unsafe_allow_html=True)

    # set_background('moneyheist.jpg')
    st.caption('This recommendations are based on the dataset provided, pls enter the movies from the dataset only..!!')
    input = st.text_input(":orange[Enter Movie Name]", placeholder='enter movie name')
    submit = None
    if input:
        submit = st.button("Submit")
    if submit:
        pipeline = RecommendationsPipeline()
        recommendations, ground_truth = pipeline.make_recommendations(movie_title=input)
        # st.warning(len(recommendations))

        if recommendations:
            
            # Determine the number of elements (handles cases with less than 10)
            num_elements = len(recommendations)

            # Create the first row with 5 columns (or less if there are fewer elements)
            cols1 = st.columns(min(5, num_elements))  # Ensures max 5 columns

            # Display data in the first row columns
            for col, text in zip(cols1, recommendations[:min(5, num_elements)]):  # Slice data for first row
                with col:
                    st.success(text)

                # Check if there are remaining elements (handles cases with less than 10)
                if num_elements >= 5:
                # Create the second row with remaining columns (or less if there are fewer elements)
                    cols2 = st.columns(min(5, num_elements - 5))  # Ensures max 5 columns

            # Display data in the second row columns
            for col, text in zip(cols2, recommendations[5:]):  # Slice data for second row
                with col:
                    st.success(text)

        else:
            st.write("No recommendations found")

except Exception as e:
    st.error("No recommendations found")