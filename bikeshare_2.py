import time
import pandas as pd
import numpy as np
import datetime

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

    while True:     # for handling the unexpected input by user
        city_input = input("Please select a city (1. Chicago, 2. New York City, or 3. Washington)")
        # checks user input, and if it is matching the cities we have, prints the city name in title case and breaks out of the loop
        if city_input.lower() in ['1', 'chicago']:
            city = 'chicago'
            print(city.title() + ', we will take a look now.')
            break
        elif city_input.lower() in ['3', 'washington']:
            city = 'washington'
            print(city.title() + ', we will take a look now.')
            break
        elif city_input.lower() in ['2', 'new york city']:
            city = 'new york city'
            print(city.title() + ', we will take a look now.')
            break
        # if they did not enter an input matching any of the cities, this will ask again
        else:
            print('Please enter only 1, 2, 3 or chicago, new york, or washington')
    while True:
       filter_input = input("Would you like to filter the data by month, day, both, or not at all (enter none)?")
       filter_input = filter_input.lower()
       if filter_input in ['month', 'day', 'both', 'none']:
            filters = filter_input
            break
       else:
            print('Please enter just one of the following: month, day, both, none')



    # get user input for month (all, january, february, ... , june)
    m_list = ['january', 'february', 'march', 'april', 'may', 'june']
    d_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if filters == 'month' or filters == 'both':
        while True:
            month_input = input("Which month - January, February, March, April, May, or June?")
            month_input = month_input.lower()
            if month_input in m_list:
                if filters == 'month':
                    month = month_input
                    day = 'all'
                    break
                elif filters == 'both':
                    month = month_input
                    break
                else:
                    print('Please enter a month you would like to filter on to contine.')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    if filters == 'day' or filters == 'both':
        while True:
            day_input = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?")
            day_input = day_input.lower()
            if day_input in d_list:
                if filters == 'day':
                    day = day_input
                    month = 'all'
                    break
                elif filters == 'both':
                    day = day_input
                    break
                else:
                    print('Please enter a day you would like to filter on to contine.')
    elif filters == 'none':
        month = 'all'
        day = 'all'
    print('TEST City selected: ', city)
    print('TEST month selected: ', month)
    print('TEST day selected :', day)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv("C:/Users/kelse/OneDrive/Desktop/Udacity/Python Project/all-project-files/" + CITY_DATA[city])
    # convert Start Time to a datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #get parts of the start time to be able to filter on
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day of Week'] = df['Start Time'].dt.day_name()
    day = day.title()
    month = month.title()




    #filter by day of week if selected
    if day != 'All':
        #Creates new dataframe with just the day of the week that is selected
        df = df[df['Day of Week'] == day]
    # filter by month if selected
    if month != 'All':
        #Creates new dataframe filtered to the month if selected
        df = df[df['Month'] == month]
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    top_month = df['Month'].mode()[0]
    print('The most popular month is:  ', top_month)

    # display the most common day of week
    top_day = df['Day of Week'].mode()[0]
    print('The most popular day of the week is:  ', top_day)


    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    top_hour = df['Hour'].mode()[0]
    print('The most popular hour is:  ', top_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    top_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is:  ', top_start_station)


    # display most commonly used end station
    top_end_station = df['End Station'].mode()[0]
    print('The most popular end station is:  ', top_end_station)

    # display most frequent combination of start station and end station trip
    df['Start and End Station'] = df['Start Station'] + ' & ' + df['End Station']
    top_start_and_end = df['Start and End Station'].mode()[0]
    print('The most popular combination of start station and end station is:  ', top_start_and_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:  ', total_travel_time)

    # display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('The average travel time is:  ', avg_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Creating variables to answer below
    user_stats = df['User Type'].value_counts()



    # Display counts of user types
    print('There are ', user_stats, 'user types.')

    # Display counts of gender, except for Washington, which doesn't have any.
    try:
        gender_stats = df['Gender'].value_counts()
        print('Gender composition: ', gender_stats)
    except:
        print('There is no gender data for this city.')

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = df['Birth Year'].min()
        recent_yob = df['Birth Year'].max()
        popular_yob = df['Birth Year'].mode()[0]
        today = datetime.date.today()
        this_year = today.year
        oldest_customer = this_year - earliest_yob
        youngest_customer = this_year - recent_yob
        print('The earliest year of birth is:  ', earliest_yob)
        print('The oldest customer is: ', oldest_customer, 'years old.')
        print ('The most recent year of birth is:  ', recent_yob)
        print('The youngest customer is: ', youngest_customer, 'years old.')
        print('The most frequent year of birth is:  ', popular_yob)
    except:
        print('There is no date of birth data for this city.')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Your script also needs to prompt the user whether they would like want to see the raw data. If the user answers 'yes,'
    then the script should print 5 rows of the data at a time, then ask the user if they would like to see 5 more rows of the data.
    The script should continue prompting and printing the next 5 rows at a time until the user chooses 'no,' they do not want any
    more raw data to be displayed.
    """
    i = 0
    show_raw_data = str(input("Would you like to view individual trip data? Please, type 'yes' or 'no'"))
    while True:
        show_raw_data = show_raw_data.lower()
        while True:
            if show_raw_data != 'yes':
                break
            if show_raw_data == 'yes':
                print(df[i:i+5])
                i += 5
                show_raw_data = input('Do you want to see more raw data?')
                show_raw_data = show_raw_data.lower()
                if show_raw_data != 'yes':
                    break
            if show_raw_data != 'yes':
                break
        if show_raw_data != 'yes':
            break



    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() not in ['yes', 'y', 'ye', 'no', 'n']:
            redoinput = input('\nPlease enter yes if you would like to restart, or no if you would like to quit.')
            if redoinput.lower() in ['no', 'n']:
                break
        elif restart.lower() not in ['yes', 'y', 'ye']:
            sure = input('\nAre you sure you would like to quit? Type yes to quit.')
            if sure.lower() in ['yes', 'y', 'ye']:
                break


if __name__ == "__main__":
	main()