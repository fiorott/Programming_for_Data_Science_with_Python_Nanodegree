import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    city_filter = ['chicago', 'new york', 'washington']
    while city not in city_filter:
        city = input("\nFilter data by city\n[ Chicago, New York or Washington ] : ").lower()


    # get user input for month (all, january, february, ... , june)
    month = None
    month_filter = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in month_filter:
        month = input("\nFilter data by month\n[ all, january, february, march, april, may, or june ] : ").lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    day_filter = ['all', '1', '2', '3', '4', '5', '6', '7']
    while day not in day_filter:
        day = input("\nFilter data by day of the week\n['all', 'sunday as 1', 'monday as 2', ...., 'saturday as 7'] : ").lower()


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

    print('Filters: [', city, ',', month, ',', day, ']')

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]


    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    # -------------------START--------------------------
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month

    # find the most most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)
    # --------------------END---------------------------


    # display the most common day of week
    # -------------------START--------------------------
    # extract day from the Start Time column to create an day_of_week column
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # find the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Popular day of the week :', popular_day)
    # --------------------END---------------------------


    # display the most common start hour
    # -------------------START--------------------------
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    # --------------------END---------------------------


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    # -------------------START--------------------------
    print('Most popular Start station: ', df['Start Station'].mode()[0])
    # --------------------END---------------------------


    # display most commonly used end station
    # -------------------START--------------------------
    print('Most popular End station: ', df['End Station'].mode()[0])
    # --------------------END---------------------------


    # display most frequent combination of start station and end station trip
    # -------------------START--------------------------
    df['route'] = df['Start Station'] + ' - ' + df['End Station']
    print('Most popular route: ', df['route'].mode()[0])
    # --------------------END---------------------------


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # Trip Duration stats:
    # -------------------START--------------------------
    print('Trip Duration stats: ')
    print('Max Travel Time: ', df['Trip Duration'].max())
    print('Min Travel Time: ', df['Trip Duration'].min())
    # display mean travel time
    print('Mean Travel Time: ', df['Trip Duration'].mean())
    print('Most Travel Time: ', df['Trip Duration'].mode()[0])
    # display total travel time
    print('Total Travel Time: ', df['Trip Duration'].sum())
    # --------------------END---------------------------


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User type stats: ')
    print(df['User Type'].value_counts())


    # Display counts of gender
    print('Gender stats: ')
    print(df['Gender'].value_counts())


    # Display earliest, most recent, and most common year of birth
    print('Age stats: ')
    print('Earliest Birth Year   : ', int(df['Birth Year'].min()))
    print('Most recent Birth Year: ', int(df['Birth Year'].max()))
    print('Most common Birth Year: ', int(df['Birth Year'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
