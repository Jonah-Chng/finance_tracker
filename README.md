# finance_tracker
Python code for converting finance data - in CSV format - to a data frame. The code then automatically categorises them with Regex and plots it in time. A pie chart with the various categories are generated every month.

# How to use your chosen csv file
Open finance.py and replace the 'input_path' variable with the full path to your chosen CSV file.

By default, the code will look for your CSV file in your directory finance.py is in. You can drop your csv file into the same directory as the finance.py and change the variable 'file_name' to match your CSV's file name. 


# Download dependencies
pip3 install pandas

# Examples
Run the code (linux and mac)
```
cd fianace_tracker/
chmod +x finance.py
python3 finance.py
```
# Notes
finance.ipynb is not updated to finance.py

# TODO
1. Code cant handle change in year well
2. Figures can only be shown one at a time