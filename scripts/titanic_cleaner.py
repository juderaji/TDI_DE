import pandas as pd
import numpy as np
import argparse
import logging

# Set up logging
logging.basicConfig(filename='titanic_cleaner.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

class TitanicCleaner:
    def __init__(self, file='./titanic.csv'):
        self.df = self.load_data(file)
        
    def load_data(self, file):
        logging.info(f"Loading data from {file}")
        return pd.read_csv(file)
    
    def fill_missing_values(self):
        logging.info("Filling missing values")
        # Correcting by assigning back to columns
        self.df['Age'].fillna(self.df['Age'].median(), inplace=True)
        self.df['Embarked'].fillna(self.df['Embarked'].mode()[0], inplace=True)
        return self.df

    def remove_duplicates(self):
        logging.info("Removing duplicates")
        self.df.drop_duplicates(inplace=True)
        return self.df

    def bin_age(self):
        logging.info("Binning Age column using apply()")
        def age_category(age):
            if age < 18:
                return '<18'
            elif age < 40:
                return '18-40'
            elif age < 60:
                return '40-60'
            else:
                return '60+'
        self.df['AgeBin'] = self.df['Age'].apply(age_category)
        return self.df

    def calculate_family_size(self):
        logging.info("Calculating Family Size using apply()")
        self.df['FamilySize'] = self.df.apply(lambda row: row['SibSp'] + row['Parch'], axis=1)
        return self.df

    def map_embarked(self):
        logging.info("Mapping Embarked column using apply()")
        embarked_map = {'S': 'Southampton', 'C': 'Cherbourg', 'Q': 'Queenstown'}
        self.df['Embarked'] = self.df['Embarked'].apply(lambda x: embarked_map.get(x, x))
        return self.df

def main():
    parser = argparse.ArgumentParser(description='Titanic Data Cleaner')
    parser.add_argument('--output', type=str, help='Path to save the cleaned data')
    parser.add_argument('--bin-age', action='store_true', help='Bin the Age column')
    parser.add_argument('--family-size', action='store_true', help='Calculate Family Size')
    parser.add_argument('--map-embarked', action='store_true', help='Map Embarked column')
    
    args = parser.parse_args()

    cleaner = TitanicCleaner()  # Uses 'titanic.csv' by default
    cleaner.fill_missing_values()
    cleaner.remove_duplicates()

    if args.bin_age:
        cleaner.bin_age()
    if args.family_size:
        cleaner.calculate_family_size()
    if args.map_embarked:
        cleaner.map_embarked()
    
    if args.output:
        cleaner.df.to_csv(args.output, index=False)
        logging.info(f'Saved cleaned data to {args.output}')
    else:
        print(cleaner.df.head())
  

if __name__ == "__main__":
    main()
