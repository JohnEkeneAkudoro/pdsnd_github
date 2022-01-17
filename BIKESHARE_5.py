import time
import pandas as pd
import numpy as np

RECORD_CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

RECORD_CITIES = ['chicago', 'new york city', 'washington']

RECORD_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

RECORD_DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def preferred_city():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # input() returns Str data type

    # Getting user input for city (Chicago, New York City and Washington)
    while True:
        try:
            city = input('Let me know if you\'d like to see records for Chicago, New York City or Washington! ').lower()	
            if city in RECORD_CITIES:
                break
        except (ValueError, KeyboardInterrupt):
            print('Your entry is invalid. You can only enter Chicago, New York City or Washington')
            print('Please enter Chicago, New York City or Washington')

    # Getting user input for month (All, January, February, ... , June)
    while True:
        try:
            month = input('Please select January, February, March, April, May or June to view data records per month. Otherwise, select \'All\' to see data records for the 6 months altogether! ').lower()	
            if month in RECORD_MONTHS:
                break
        except (ValueError, KeyboardInterrupt):
            print('Your entry is invalid. You can only enter January, February, March, April, May, June or All')
            print('Please enter January, February, March, April, May, June or All')

    # Getting user input for day of the week (All, Sunday, Monday, ... , Saturday)
    while True:
        try:
            day = input('Finally: Please select Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday to view data records per day of the week. Otherwise, select \'All\' to see data records for the 7 days in a week altogether ').lower()	
            if day in RECORD_DAYS:
                break
        except (ValueError, KeyboardInterrupt):
            print('Your entry is invalid. You can only enter Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or All')
            print('Please enter Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or All')


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
    # Loading of data file into a dataframe
    df = pd.read_csv(RECORD_CITY_DATA[city])

    # Converting of Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extracting of month and day of the week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_the_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # Filtering by month if applicable
    if month != 'all':
        # Using the index of the list of months to get the corresponding int
        month = RECORD_MONTHS.index(month) + 1

        # Filtering by month to create the new dataframe
        df = df[df['month'] == month] 

    # Filtering by day of week if applicable
    if day != 'all':
        # Filtering by day of the week to create the new dataframe
        df = df[df['day_of_the_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Displaying Top 3 most frequent month

    most_frequent_month = df['month'].value_counts().nlargest(3)
    print('Most frequent month is: \n' + str(most_frequent_month))

    # Displaying Top 3 most frequent day of the week

    most_frequent_day_of_the_week = df['day_of_the_week'].value_counts().nlargest(3)
    print('Most frequent day of the week is: \n' + str(most_frequent_day_of_the_week))

    # Displaying Top 3 most frequent start hour

    most_frequent_start_hour = df['hour'].value_counts().nlargest(3)
    print('Most frequent start hour is: \n' + str(most_frequent_start_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Displaying Top 3 most frequently used start station

    most_frequent_start_station = df['Start Station'].value_counts().nlargest(3)
    print('Most frequent start station is: \n' + str(most_frequent_start_station))

    # Displaying Top 3 most frequently used end station

    most_frequent_end_station = df['End Station'].value_counts().nlargest(3)
    print('Most frequent end station is: \n' + str(most_frequent_end_station))

    # Displaying top most frequent combination of start station and end station trip

    most_frequent_start_end_combination = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)

    # OR

    most_frequent_start_end_combination = df.groupby(['Start Station', 'End Station',], sort=False).size()
    print('Most frequent start hour is: \n' + str(most_frequent_start_end_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Displaying the total travel time
    sum_travel_time = df['Trip Duration'].sum()
    print('Total travel time is ' + str(sum_travel_time))

    # Displaying the mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is ' + str(average_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Displaying counts of user types
    user_types_counts = df['User Type'].value_counts()
    print('Counts of user types is: /n' + str(user_types_counts))

    # Displaying counts of gender
    # Remembering that Gender columns is present in Chicago & New York City Dictionary Keys and not present in Washington Dictionary Key
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('Counts of gender is: /n' + str(gender_counts))
        print('Note that Gender data is ONLY available in Chicago and New York City')

    # Displaying earliest, most recent, and Top 3 most common year of birth
    # Remembering that Birth Year columns is present in Chicago & New York City Dictionary Keys and not present in Washington Dictionary Key
    if 'Birth Year' in df.columns:
        earliest_birth_year = df['Birth Year'].min()
        print('Earliest year of birth is ' + str(earliest_birth_year))

        most_recent_birth_year = df['Birth Year'].max()
        print('Most recent year of birth is ' + str(most_recent_birth_year))

        most_common_birth_year = df['Birth Year'].value_counts().nlargest(3)
        print('Most common year of birth is: /n' + str(most_common_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Raw data is displayed upon the request of the user.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """    
    start_loc = 0
    while True:
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
        if view_data != 'yes':
            break
        start_loc += 5
        print(df.iloc[0:5])
        
        
def main():
    while True:
        city, month, day = preferred_city()
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