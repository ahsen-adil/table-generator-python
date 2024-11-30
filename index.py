import streamlit as st
import pandas as pd  

def main():
    st.title("🧮 Multiplication Table Generator")
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #f0f2f6; 
        }
        .title {
            color: #FF5733; 
            font-size: 40px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.subheader("Enter a number below to generate its multiplication table:")
    
    number = st.number_input("Enter a number:", min_value=1, step=1, value=1)

    if st.button("Generate Table"):
        table_data = {"Multiplier": [], "Result": []}
        for i in range(1, 11):
            table_data["Multiplier"].append(f"{number} x {i}")
            table_data["Result"].append(number * i)

        df = pd.DataFrame(table_data)

        st.markdown("### Multiplication Table:")
        st.dataframe(df.style.set_properties(**{
            'background-color': '#ffffff',
            'color': '#333',
            'border': '1px solid #ddd',
            'text-align': 'center',
        }))

if __name__ == "__main__":
    main()
