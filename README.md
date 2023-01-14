# SQLearn 
A personal place to test and learn about SQL commands
<video src="https://user-images.githubusercontent.com/90710790/212494264-5a9489a4-a14d-41dd-853f-bb996de12469.mp4" controls></video>



## Customizing the dataset
```
git clone https://github.com/ArshS1/SQLearn
cd SQLearn/data/
rm -f data.sqlite

# Visit https://www.rebasedata.com/ to convert your .sql to .sqlite and put it in the data directory
# Open app.py and visit line 7 and make the necessary changes

connection = sqlite3.connect(<Insert File Path for .sqlite>)
```

## Run the program
``` 
streamlit run app.py
```
