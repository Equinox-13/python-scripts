import pandas as pd

df = pd.read_csv('covid_19_data.csv')
df['Country/Region'] = df['Country/Region'].str.lower()
df['Last Update'] = pd.to_datetime(df['Last Update'])
ans=True
while ans:
    print("""
    1.Display current global counts
    2.Check for a Country/Region
    3.Check history for a Country/Region
    4.Exit/Quit
    (Select option from 1-4)
    """)
    ans = input("What would you like to do? ")

    if ans == "1":
      confirmed = df['Confirmed'].sum()
      death = df['Deaths'].sum()
      recovered = df['Recovered'].sum()
      print("==============================")
      print(f"Confirmed: {confirmed}")
      print(f"Deaths: {death}")
      print(f"Recovered: {recovered}")
      print("==============================")

    elif ans == "2":
      country_region = input("Enter a Country/Region name:")
      country_region = country_region.lower()
      if country_region in df.values:
        sub_df = df.loc[df["Country/Region"] == country_region]
        confirmed = sub_df['Confirmed'].sum()
        death = sub_df['Deaths'].sum()
        recovered = sub_df['Recovered'].sum()
        print("==============================")
        print(f"Confirmed: {confirmed}")
        print(f"Deaths: {death}")
        print(f"Recovered: {recovered}")
        print("==============================")
      else:
        print("!!!! Please check your input !!!!")

    elif ans == "3":
      country_region = input("Enter a Country/Region name:")
      country_region = country_region.lower()
      if country_region in df.values:
        sub_df = df.loc[df["Country/Region"] == country_region]
        sub_df = sub_df[['Last Update','Confirmed','Deaths','Recovered']]
        sub_df.sort_values(by=['Last Update'], inplace=True, ascending=False)
        print(sub_df.to_string(index=False))
      else:
        print("!!!! Please check your input !!!!")

    elif ans == "4":
      print("\n Goodbye")
      ans = None
    else:
        print("\n Not Valid Choice Try again")
