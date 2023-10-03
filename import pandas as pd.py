import pandas as pd
import numpy as np


csv_file_path = r"C:\Users\qaism\OneDrive - University of Virginia\Documents\Class Documents\DS 3001\assignment2\data\airbnb_hw.csv"
airbnb_df = pd.read_csv(csv_file_path)
airbnb_df[['Price']].head()

unique_prices = airbnb_df['Price'].unique()
sorted(unique_prices)[:20], sorted(unique_prices)[-20:]

airbnb_df['Price'] = airbnb_df['Price'].str.replace(',', '')
airbnb_df['Price'] = pd.to_numeric(airbnb_df['Price'], errors='coerce')
missing_values_count = airbnb_df['Price'].isna().sum()
print(missing_values_count)


sharks_csv_file_path = r'C:\Users\qaism\OneDrive - University of Virginia\Documents\Class Documents\DS 3001\assignment2\data\sharks.csv'
sharks_df = pd.read_csv(sharks_csv_file_path)
unique_types = sharks_df['Type'].unique()

non_string_types = [x for x in unique_types if not isinstance(x, str)]
string_types = [x for x in unique_types if isinstance(x, str)]
sorted_string_types = sorted(string_types)
non_string_types, sorted_string_types

sharks_df['Type'] = sharks_df['Type'].fillna('Unknown')
sharks_df['Type'] = sharks_df['Type'].str.replace('Boat.*', 'Boating', regex=True) 
type_mapping = {
    'Invalid': 'Ambiguous',
    'Unconfirmed': 'Ambiguous',
    'Unverified': 'Ambiguous',
    'Questionable': 'Ambiguous',
    'Under investigation': 'Under Investigation'
}
sharks_df['Type'] = sharks_df['Type'].replace(type_mapping)
cleaned_unique_types = sharks_df['Type'].unique()
sorted(cleaned_unique_types)


pretrial_csv_file_path =  r"C:\Users\qaism\OneDrive - University of Virginia\Documents\Class Documents\DS 3001\assignment2\data\VirginiaPretrialData2017.csv"
pretrial_df = pd.read_csv(pretrial_csv_file_path)
unique_pretrial_values = pretrial_df['WhetherDefendantWasReleasedPretrial'].unique()
sorted([str(x) for x in unique_pretrial_values])

pretrial_df['WhetherDefendantWasReleasedPretrial'] = pretrial_df['WhetherDefendantWasReleasedPretrial'].replace('9', np.nan)
pretrial_df['WhetherDefendantWasReleasedPretrial'] = pd.to_numeric(pretrial_df['WhetherDefendantWasReleasedPretrial'], errors='coerce')
missing_values_pretrial = pretrial_df['WhetherDefendantWasReleasedPretrial'].isna().sum()
missing_values_pretrial


unique_imposed_sentence = pretrial_df['ImposedSentenceAllChargeInContactEvent'].unique()
unique_sentence_type = pretrial_df['SentenceTypeAllChargesAtConvictionInContactEvent'].unique()
sorted_unique_imposed_sentence = sorted([str(x) for x in unique_imposed_sentence])
sorted_unique_sentence_type = sorted([str(x) for x in unique_sentence_type])

sorted_unique_imposed_sentence[:20], sorted_unique_imposed_sentence[-20:], sorted_unique_sentence_type

pretrial_df['ImposedSentenceAllChargeInContactEvent'].replace(' ', np.nan, inplace=True)
pretrial_df['ImposedSentenceAllChargeInContactEvent'] = pd.to_numeric(pretrial_df['ImposedSentenceAllChargeInContactEvent'], errors='coerce')

condition = pretrial_df['SentenceTypeAllChargesAtConvictionInContactEvent'].isin([9, 4])
pretrial_df.loc[condition, 'ImposedSentenceAllChargeInContactEvent'] = np.nan
final_missing_values_imposed_sentence = pretrial_df['ImposedSentenceAllChargeInContactEvent'].isna().sum()



