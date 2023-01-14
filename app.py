# import packages
import streamlit as st
import pandas as pd

# database management

def main():
    # setup main page
    st.title("SQLearn")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("HomePage")

        # setup the layout
        columnOne, columnTwo = st.columns(2)
        
        print(type(columnOne))
        with columnOne:
                rawFormat = st.text_area("Enter SQL Command")
                runCommand = st.form("Execute")

        # Results
        with columnTwo:
            if runCommand:
                st.info("Query Executed")
                # allow user to copy the query
                st.code(rawFormat)

    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
