import time
import sys
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) time_filter - determine duration of time to include month, day, or all available data; also identify input errors
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\n\n\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("\nWhich city would you like Bikeshare data?  \nPlease enter Chicago, New York City, or Washington: ").lower()
        except ValueError:
            print('\nI did not recognize that city. Please try again.')
        if city == 'chicago':
            print("\nGathering data for Chicago!\n")
        elif city == 'new york city':
            print("\nGathering data for New York City!\n")
        elif city == 'washington':
            print("\nGathering informaton on Washington!\n")
        else:
            print("\nI did not recognize that city. Please restart application.")
            sys.exit()
        
    # get user input for month (all, january, february, ... , june)
        try:
            month = input("\nWould you like to filter the data for a specific month or all available months?  \nPlease enter January, February, March, April, May, June, or all: ").lower()
        except ValueError:
            print('I did not recognize that month.  Please restart.')
        if month == 'january':
            print("Gathering information during the month of January!\n")
        elif month == 'february':
            print("Gathering information during the month of February!\n")       
        elif month == 'march':
            print("Gathering information during the month of March!\n")
        elif month == 'april':
            print("Gathering information during the month of April!\n")
        elif month == 'may':
            print("Gathering information during the month of May!\n")
        elif month == 'june':
            print("Gathering information during the month of June!\n")
        elif month == 'all':
            print("Gathering informatin for all available months!\n")
        else:
            print("I did not recognize that month.  Please restart application.")
            sys.exit()
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
        try:
            day = input("\nWhat day of the week would you like information?  \nPlease type Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all to include all days: ").lower()  
        except ValueError:
            print('\nI did not recognize that day.  Please restart.')
        if day == 'monday':
            print("\nGathering information for Monday!\n")
        elif day == 'tuesday':
            print("\nGathering information for Tuesday!\n")       
        elif day == 'wednesday':
            print("\nGathering information for Wednesday!\n")
        elif day == 'thursday':
            print("\nGathering information for Thursday!\n")
        elif day == 'friday':
            print("\nGathering information for Friday!\n")
        elif day == 'saturday':
            print("\nGathering information for Saturday!\n")
        elif day == 'sunday':
            print("\nGathering information for Sunday!\n")
        elif day == 'all':
            print("\nGathering information for all available days!")
        else:
            print("\nI did not recognize that day.  Please restart application.")
            sys.exit()
        
        print('-'*40)
        return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   
    # Load the user selected city's csv data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time column into datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    # filter by month if applicable
    if month != 'all':
         # use the index of the months list to get the corresponding integer
         months = ['january', 'february','march', 'april', 'may', 'june']
         month = months.index(month) + 1
         df = df[df['month'] == month]
         
         #filter by month to create the new dataframe
         df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':

    # filter by day of week to create the new dataframe
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday']
        day = days.index(day)
        df = df[df['day_of_week'] == day]
    
    # filter by month to creat the new dataframe
        df = df[df['day_of_week'] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
       
    # display the most common month
    month_counts = df['month'].value_counts()
    most_common_month = month_counts.idxmax()
    
    # popular_month = df['month'].mode()[0]
    print("The most common month is:", most_common_month)
    
    # display the most common day of week
    if df['day_of_week'].empty:
        print("Unfortunately, data is not available. Please try another inquiry.")
    else:
        day_of_week_counts = df['day_of_week'].value_counts()
        most_common_day_of_week = day_of_week_counts.idxmax()
        # popular_day = df['day_of_week'].mode()[0]
        print("The most common day of the week is: ", most_common_day_of_week)

    # display the most common start hour
    if df['hour'].empty:
        print("Unfortunately, data is not available. Please try another inquiry.")
    else:
        hour_counts = df['hour'].value_counts()
        most_common_hour_of_day = hour_counts.idxmax()
        # popular_hour = df['hour'].mode()[0]
        print("The most common hour of the day is:", most_common_hour_of_day,": 00 hours")

    print('-'*40)

    # continuation message to limit amount of information on screen
    continuation_message = input("\nWould you like to see additional information?  Enter yes or no\n")
    if continuation_message.lower() == 'no':
        sys.exit()
        

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station_counts = df['Start Station'].value_counts()
    most_common_start_station = start_station_counts.idxmax()
    print("The most commonly used start station is: ", most_common_start_station)

    # display most commonly used end station
    end_station_counts = df['End Station'].value_counts()
    most_common_end_station = end_station_counts.idxmax()    
    print("The most commonly used end station is: ", most_common_end_station)
    
    # display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station','End Station']).size().idxmax()
    print("\nThe most frequently used trip combination from start to end is:")
    print(most_frequent_combination)
    
    print('-'*40)

    # continuation message to limit amount of information on screen
    continuation_message = input("\nWould you like to see additional information?  Enter yes or no\n")
    if continuation_message.lower() == 'no':
        sys.exit()

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum(axis=0)
    
    # calculate the total travel time from seconds into hours, minutes, seconds
    total_duration_hours = total_travel // 3600  
    total_duration_minutes = (total_travel % 3600) // 60
    total_duration_seconds = round((total_travel % 3600) % 60)
    print("The total travel time is:", total_duration_hours, "hours,", total_duration_minutes,"minutes,", total_duration_seconds, "seconds")

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    
    # calculate the average trip time from seconds into hours, minutes, seconds
    total_average_trip_hours = mean_travel // 3600  
    total_average_trip_minutes = (mean_travel % 3600) // 60
    total_average_trip_seconds = round((mean_travel % 3600) % 60)
    print("The average trip time is:", total_average_trip_hours, "hours,", total_average_trip_minutes,"minutes,", total_average_trip_seconds, "seconds")

    print('-'*40)
    
    # continuation message to limit amount of information on screen
    continuation_message = input("\nWould you like to see additional information?  Enter yes or no\n")
    if continuation_message.lower() == 'no':
        sys.exit()

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    if 'User Type' in df.columns:
        df.fillna(0, inplace = False)
        user_type = df['User Type'].value_counts()
        print("The number of users based on:", user_type)
    else:
        print("The 'User Type' column is not available in the DataFrame")

    # Display counts of gender
    if 'Gender' in df.columns:
        df.fillna(0, inplace = False)
        gender_count = df['Gender'].value_counts()
        print("\nThe number of users based on:", gender_count)
    else:
        print("The 'Gender' column is not available in the DataFrame.")
    
    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        df.fillna(0, inplace = False)
        earliest_birth_year = round(df['Birth Year'].min())
        latest_birth_year = round(df['Birth Year'].max())
        most_common_birth_year_count = round(df['Birth Year'].value_counts().idxmax())
        print("\nThe eldest user was born in", earliest_birth_year)
        print("The youngest user was born in", latest_birth_year)
        print("The most common birth year is", most_common_birth_year_count)
        print('-'*40)
    else:
        print("The 'Birth Year' column is not available in the DataFrame.")

def display_data(df):
    # Displays raw data for based on the data filters provided by the user
    # Get total number of rows in the dataframe
    total_rows_in_dataframe = len(df)

    # Establish a varible for number of displayed rows of raw.  Setting variable so it can be configurable in future releases instead of hard coded
    number_of_rows_to_display = 5
    # Prompt user if they want to see raw data
    raw_data_prompt = input("Do you want to see the first 5 rows of data?  Please enter yes or no. ")

    # Loop through dataframe at an increment of the number_of_rows_to_display variable
    while raw_data_prompt.lower() == 'yes':
        for i in range(0, total_rows_in_dataframe, number_of_rows_to_display):
            print(df.iloc[i:i+number_of_rows_to_display])
            print('\n')

    # Request input from user if they want to see another iteration of raw data
            next_five_raw_data_rows = input("\nWould you like to see an additional 5 rows of raw data? Please enter yes or no: ")
    # If user input is anyting other than yes, then end application
            if next_five_raw_data_rows != 'yes':
                print("\nThank you for utilizing the Bikeshare application.")
                sys.exit()                
    # If user input indicates they want the next iteration of data displayed, continue loop until all raw data is displayed
            else:
                if i != total_rows_in_dataframe:
                    print("The next iteration of data is as follows: ")
                else:
                    print("\nThere is no additional data to display")
        return
             
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()