import streamlit as st
from PIL import Image

st.title('Product Showcase - Add Your Product')#js-repo-pjax-container
# Create a file uploader
j = "https://github.com/PB-byt/ecom_product_pics/blob/bfd5ea9e224baefc9805ba093c558e09d1addb22/image_search_1732589999492.jpg"#js-repo-pjax-container
st.image("https://raw.githubusercontent.com/PB-byt/ecom_product_pics/main/image_search_1734490759482.jpg",caption="git hub pic")
uploaded_file = st.file_uploader("Choose a product image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    # You can also save the image locally if needed
    # image.save(f"your_directory/{uploaded_file.name}")
# Additional fields for product details
product_name = st.text_input('Product Name')
product_price = st.number_input('Product Price', min_value=0.00, step=0.01)

if st.button('Submit'):
    st.write(f'Product Name: {product_name}')
    st.write(f'Product Price: ${product_price}')
    st.write('Product image uploaded successfully!')
