import streamlit as st
import pandas as pd

# Set layout to use the full width of the page
st.set_page_config(layout="wide")

# Title of the application
st.title('Data Uploader and Viewer')

# File uploader
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

# Input for the separator
separator = st.text_input("Specify the separator used in the file (default is comma ','):", ",")

# If a file is uploaded, load the data
if uploaded_file is not None:
    try:
        # Identify the file type and load accordingly
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file, sep=separator)
        else:
            df = pd.read_excel(uploaded_file)

        st.write("### Data preview:")
        st.dataframe(df)

        # Check for numeric and categorical columns
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
        numeric_columns_with_variation = [col for col in numeric_columns if df[col].nunique() > 1]
        categorical_columns = df.select_dtypes(include=['object', 'category']).columns

        # Show both filters if both types of columns exist and have valid data
        if len(numeric_columns_with_variation) > 0 and len(categorical_columns) > 0:
            col1, col2 = st.columns(2)

            # --- Numeric Filters ---
            with col1:
                st.write("### Filter the numeric data:")
                filter_column = st.selectbox("Select a numeric column to filter", numeric_columns_with_variation)

                if filter_column:
                    min_value = float(df[filter_column].min())
                    max_value = float(df[filter_column].max())

                    min_value, max_value = st.slider(
                        f"Select the range of values for {filter_column}",
                        min_value,
                        max_value,
                        (min_value, max_value)
                    )

                    filtered_df = df[(df[filter_column] >= min_value) & (df[filter_column] <= max_value)]
                    st.write(f"### Filtered data in {filter_column} between {min_value} and {max_value}:")
                    st.dataframe(filtered_df)

            # --- Categorical Filters ---
            with col2:
                st.write("### Filter the categorical data:")
                filter_categorical_column = st.selectbox("Select a categorical column to filter", categorical_columns)

                if filter_categorical_column:
                    unique_values = df[filter_categorical_column].unique()
                    selected_values = st.multiselect(
                        f"Select values for {filter_categorical_column}",
                        unique_values,
                        default=unique_values
                    )
                    filtered_df = df[df[filter_categorical_column].isin(selected_values)]
                    st.write(f"### Filtered data in {filter_categorical_column} for selected values:")
                    st.dataframe(filtered_df)

        # Show only numeric filters if there are valid numeric columns
        elif len(numeric_columns_with_variation) > 0:
            st.write("### Filter the numeric data:")
            filter_column = st.selectbox("Select a numeric column to filter", numeric_columns_with_variation)

            if filter_column:
                min_value = float(df[filter_column].min())
                max_value = float(df[filter_column].max())

                min_value, max_value = st.slider(
                    f"Select the range of values for {filter_column}",
                    min_value,
                    max_value,
                    (min_value, max_value)
                )
                filtered_df = df[(df[filter_column] >= min_value) & (df[filter_column] <= max_value)]
                st.write(f"### Filtered data in {filter_column} between {min_value} and {max_value}:")
                st.dataframe(filtered_df)

        # Show only categorical filters if there are categorical columns
        elif len(categorical_columns) > 0:
            st.write("### Filter the categorical data:")
            filter_categorical_column = st.selectbox("Select a categorical column to filter", categorical_columns)

            if filter_categorical_column:
                unique_values = df[filter_categorical_column].unique()
                selected_values = st.multiselect(
                    f"Select values for {filter_categorical_column}",
                    unique_values,
                    default=unique_values
                )
                filtered_df = df[df[filter_categorical_column].isin(selected_values)]
                st.write(f"### Filtered data in {filter_categorical_column} for selected values:")
                st.dataframe(filtered_df)

        # Show warning if no valid columns for filtering are present
        else:
            st.warning("No numeric or categorical columns with sufficient variation to filter.")

    except Exception as e:
        st.error(f"Error loading the file: {e}")

else:
    st.write("Please upload a data file.")
