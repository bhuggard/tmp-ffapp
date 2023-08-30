import streamlit as st
import pandas as pd
import os

# Load your CSV files into DataFrames
csv_files = ["espn_clean.csv", "fantasypros_clean.csv", "fantraxhq_clean.csv", "pff_clean.csv", "rotoballer_clean.csv"]
dataframes = [pd.read_csv(file) for file in csv_files]

# Capitalize the first and last name
def capitalize_name(name):
    words = name.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

# Create a Streamlit app
def main():
    st.title("2023 Full PPR Fantasy Football Ranking Comparison App")
    # st.image("images/gsaL.png", use_column_width=True)
    
    # User input without suggestions
    name = st.text_input("Enter a name:", key="name_input")
    
    if name:
        capitalized_name = capitalize_name(name)
        display_rankings(capitalized_name)

# Function to display rankings
def display_rankings(name):
    st.header(f"Rankings for {name}")
    
    # Dictionary to map CSV filenames to source names
    source_names = {
        "espn_clean.csv": "ESPN",
        "fantasypros_clean.csv": "Fantasy Pros",
        "fantraxhq_clean.csv": "Fantrax HQ",
        "pff_clean.csv": "PFF",
        "rotoballer_clean.csv": "Rotoballer"
    }
    
    for idx, df in enumerate(dataframes):
        csv_filename = csv_files[idx]
        source_name = source_names.get(csv_filename, "Unknown Source")
        st.subheader(f"Source: {source_name}")
        
        if "Player" in df.columns:
            matching_rows = df[df["Player"].str.lower() == name.lower()]
            
            if not matching_rows.empty:
                row = matching_rows.iloc[0]
                st.write(f"Exact Match: {row['Player']}")
                st.write(f"Overall Rank: {row['Overall Rank']}")
                st.write(f"Position Rank: {row['Position Rank']}")
            else:
                st.write("No matching name found in this DataFrame")
        else:
            st.write("DataFrame structure is not as expected")

if __name__ == "__main__":
    main()
