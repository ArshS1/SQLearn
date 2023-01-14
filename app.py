# import packages
import streamlit as st
import pandas as pd

# database management
import sqlite3
connection = sqlite3.connect("data/data.sqlite")
cursor = connection.cursor()

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

        # Results of the command
        with columnTwo:
            if runCommand:
                st.info("Query Executed")
                # allow user to copy the query
                st.code(rawFormat)

    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
