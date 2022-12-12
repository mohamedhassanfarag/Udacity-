import time
import pandas as pd
import numpy as np

CITY_DATA = { 'a': 'chicago.csv',
              'b': 'new_york_city.csv',
              'c': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=input("\n please choose the city to know more data about it.\n please select a, b or c \n a) Chicago \n b) New York City \n c) Washington \n").lower()
    while city not in CITY_DATA.keys() :
        city=input('please enter a valid value (a, b or c)\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    months=['january','february','march','april','may','june','all']
           
    while True :
        month=input('Which Month do you want from following months?  (you can select "all" for no months filter) \n-January\n-February\n-March\n-April\n-May\n-June\n-All\n\n').lower()
        if month not in months:
            print('please enter a valid month as mentioned before\n')
        else :
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')

    day = input('which week day do you want? ( you can select all for no week day filter) \nSaturday\nSunday\nMonday\nTuesday\nWednesdy\nThursday\nFriday\nAll\n\n').lower()

    while day not in days :
        day=input('please enter a valid day as perviously mentioned\n')
        
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
    df=pd.read_csv(CITY_DATA[city])
    #extract month and day 
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name
    #filteration by month 
    if month != 'all' :
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        
        df= df[df['month']==month]
    #filteration  by day
    if day!='all':
        df=df[df['day']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month      
    print('the most common month is',df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('\nthe most common day of week is',df['day'].mode()[0])


    # TO DO: display the most common start hour
    print('\nthe most common start hour is',df['Start Time'].dt.hour.mode()[0])
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('the most commonly used start station is ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('\nthe most commonly used end station is ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station'] + ' --- '+df['End Station']
    print('\nthe most frequent combination of start station and end station trip is ',df['combination'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time is',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('\naverage travel time is ',df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertype=df['User Type'].value_counts().to_frame()
    print('counts of user types are\n\n',usertype)


    # TO DO: Display counts of gender
    if 'Gender' not in df:
        print('\nSorry! we don\'t have any "Gender" data about Washington, DC')
    else:
        gendertype=df['Gender'].value_counts().to_frame()
        print('\n\ncounts of gender are\n\n',gendertype)
            
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('\nSorry! we don\'t have any "Birth year" data about Washington, DC')
    else:
        earlest=df['Birth Year'].max()
        print('\nthe earliest year of birth is ',earlest)
        recent=df['Birth Year'].min()
        print('\nthe most recent year of birth is ',recent)
        common=df['Birth Year'].mode()[0]      
        print('\nthe most common year of birth is ',common)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def return_row_data(df):
    i=0
    answer=input('Do you want to see the raw data ? (yes/no)\n').lower()
    while answer not in ['yes','no'] :
        answer =input('please answer with yes or no\n').lower()
    while True :
        if answer == 'yes' :
            print(df.iloc[i:i+5])
            i+=5
            answer=input('Do you need to see more raw data? (yes/no)\n').lower()
        else :
            print('\nYou\'re welcome!\n')
            break
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        return_row_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
