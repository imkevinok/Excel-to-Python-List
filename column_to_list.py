
import pandas as pd # STEP 1: pip install pandas 



def get_column_from_excel(file_path):
    df = pd.read_excel(file_path)
   # STEP 2: Pick which column you want to extract and change the number in "column = df.iloc[:, #].tolist()"
   # index of Excel columns:
# A -> 0
# B -> 1        
# C -> 2
# D -> 3
#ect..
    column = df.iloc[:, 1].tolist() # replace number with column you want to extract (current number 1 will grab column B)
    column_cleaned = [cell for cell in column if isinstance(cell, str)]  
    return column_cleaned


# STEP 3: Replace with path to your Excel file | My terminal threw errors when I pasted the regular path so use \\ instead of "\" or "/" if yours doesnt work too
file_path = "C:\\Users\\YOU\\PATH\\TO\\EXCEL\\FILE\\YOUR_FILE.xlsx"



list_cleaned = get_column_from_excel(file_path)

# Print the cleaned list of ticker symbols
print(list_cleaned)
