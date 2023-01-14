# import packages
import streamlit as st
import pandas as pd

# database management

def main():
    st.title("SQLearn")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("HomePage")

        # setup the layout
        
    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
