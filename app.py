import pandas as pd
import streamlit as st

def load_data(file_input, input_type):
    if input_type == 'path':
        # Determine file type based on file extension
        if file_input.endswith('.csv'):
            return pd.read_csv(file_input)
        elif file_input.endswith('.xlsx') or file_input.endswith('.xls'):
            return pd.read_excel(file_input)
        else:
            raise ValueError("Unsupported file format for file path.")
    elif input_type == 'upload':
        # Determine file type based on MIME type
        if 'csv' in file_input.type:
            return pd.read_csv(file_input)
        elif 'excel' in file_input.type or 'spreadsheetml.sheet' in file_input.type:
            return pd.read_excel(file_input)
        else:
            raise ValueError("Unsupported file format for uploaded file.")
    else:
        raise ValueError("Invalid input type for loading data.")

def main():
    st.title("Data Viewer App")
    input_type = st.radio("Please choose input type", ["Upload File", "Enter File Path"])

    if input_type == 'Enter File Path':
        file_path = st.text_input("Enter the path to your file:")
        if st.button("Load Data"):
            try:
                data = load_data(file_path, 'path')
                st.write("Data Loaded Successfully!")
                with st.expander("Please open to see your data"):
                    st.dataframe(data, use_container_width=True)
            except Exception as e:
                st.error(f"Failed to load data: {str(e)}")

    elif input_type == 'Upload File':
        uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "xls"])
        if uploaded_file is not None:
            try:
                data = load_data(uploaded_file, 'upload')
                st.write("Data Loaded Successfully!")
                with st.expander("Open the expander to preview your data"):
                    st.dataframe(data.head(), use_container_width=True)
            except Exception as e:
                st.error(f"Failed to load data: {str(e)}")

if __name__ == "__main__":
    main()
