
import numpy as np



def dataclean(df):


    # Copy the year of manufacture to a new column "Year". convert it to interger and remove it from "Model"
    df['Year'] = df.Model.str[8:]
    df['Year'] = df['Year'].astype(int)
    df['Model'] = df.Model.str[:7]


    # Create temp column and fill base on car manufacture year

    df['temp'] = np.where(df['Year']>= 2018, "Normal", "None")
    df['Membership'].fillna(df.temp, inplace=True)
    df.drop(columns=['temp'], inplace=True)

    # Drop the rows which as duplicated "Car ID"
    df.drop_duplicates(subset=['Car ID'], inplace=True)

    # Create a new "units" column and copy units
    df['units'] = df.Temperature.str[-2:]

    # Remove the units from "Temperature" column
    df['Temperature'] = df.Temperature.str[:5]

    # Convert string to float
    df['Temperature'] = df['Temperature'].astype(float)

    # Convert "Temperature" to °C if the "units" is  °F and remove the "units" column
    df.loc[(df.units == "°F"), 'Temperature'] = round((df.Temperature-32)*5/9,1)
    df.drop(columns=["units"], inplace=True)

    # Convert  negative "RPM" to positive and remove the "temp" column
    df['temp'] = np.where(df['RPM']>= 0, "Pos", "Neg")
    df.loc[(df.temp == "Neg"), 'RPM'] = df.RPM * -1
    df.drop(columns=["temp"], inplace=True)
    
    # Create a new column "Failure" which has represented by "0" if there are no failures and "1" if it has any one of the 5 failures
    df["Failure"] = df["Failure A"] | df["Failure B"]| df["Failure C"]| df["Failure D"]

    # Dropped unwanted columns
    df = df.drop(["Car ID", "Color", "Failure A", "Failure B", "Failure C", "Failure D", "Failure E", "Year" ] , axis = 1)

    # Dropped temperature above 140
    df.drop(df[df['Temperature'] > 140].index, inplace = True)

    return df


# Make dictionaries for ordinal features

usage_map = {
    "Low":      1,
    "Medium":   2,
    "High":     3
}


membership_map = {
    "Premium":      1,
    "Normal":   2,
    "None":     3
}
# Transform ordinal features into numerical features

def encode(df):
    df.loc[:,"Usage"] = df["Usage"].map(usage_map)
    df.loc[:,"Membership"] = df["Membership"].map(membership_map)

  
    return df