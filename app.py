# import packages
import streamlit as st
import pandas as pd

# database management
import sqlite3
connection = sqlite3.connect("data/data.sqlite")
cursor = connection.cursor()

# execute commands 
def run_sqlCommands(raw: str) -> str:
    cursor.execute(raw)
    output = cursor.fetchall()
    return output

# original table info
user_details = ["user_id", "username", "first_name", "last_name", "gender", "password", "status"]

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
            with st.form(key="Query Form"):
                rawFormat = st.text_area("Enter SQL Command")
                runCommand = st.form_submit_button("Execute")
            with st.expander("Original Table Details"):
                tableInfo = {"Dataset Name: user_details": user_details}
                st.json(tableInfo)

        # Results of the command
        with columnTwo:
            if runCommand:
                st.info("Query Executed")  
                # allow user to copy the query
                st.code(rawFormat)

                queryOutput = run_sqlCommands(rawFormat)
                with st.expander("Output"):
                    st.write(queryOutput)

                with st.expander("Clean Table"):
                    convertOutput = pd.DataFrame(queryOutput)
                    st.dataframe(convertOutput)

    else:
        st.subheader("About")

if __name__ == "__main__":
    main()
