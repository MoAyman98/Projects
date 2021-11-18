import time
import pandas as pd
import numpy as np
import os
import sys

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def get_filters():



    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city=input('Which city would you prefer to look into? washington , new york city or chigaco ').lower()
        if city == "washington" or city=='new york city' or city=='chigaco':
            city = city
            break
        else:
            print("\nThat is incorrect, please try again.\n")


    # get user input for month (all, january, february, ... , june)
    while True:
        month=input('Which month you prefer to filter with? if none kidly type all ').lower()
        if month in ['january','february','march','april','may','june','july','august','september','october','november','december','all']:
            month = month
            break
        else:
            print("\nThat is incorrect, please try again.\n")    


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input('Which day you prefer to filter with? if none kidly type all ').lower()
        if day in ['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']:
            day = day
            break
        else:
            print("\nThat is incorrect, please try again.\n")

    print('-'*40)
    return city, month, day
x=get_filters()
def load_data(x):
    df=pd.read_csv(CITY_DATA[x[0]])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['week day']=df['Start Time'].dt.weekday
    df['hour']=df['Start Time'].dt.hour
    MONTH_NAME = {'january':'1','february':'2','march':'3','april':'4','may':'5','june':'6','july':'7','august':'8','september':'9','october':'10','november':'11','december':'12'}
    DAY_NAME = {'monday':'0','tuesday':'1','wednesday':'2','thursday':'3','friday':'4','saturday':'5','sunday':'6'}

    if x[1]!= 'all':
        df=df[df['month']==int(MONTH_NAME[x[1]])]
    if x[2]!= 'all':
        df=df[df['week day']==int(DAY_NAME[x[2]])]

   
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df
data=load_data(x)
def time_stats(data):
    """Displays statistics on the most frequent times of travel."""

    MONTH_NA = {1:'january',2:'february',3:'march',4:'april',5:'may',6:'june',7:'july',8:'august',9:'september',10:'october',11:'november',12:'december'}
    DAY_NA = {0:'monday',1:'tuesday',2:'wednesday',3:'thursday',4:'friday',5:'saturday',6:'sunday'}

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('Most common month:',MONTH_NA[data['month'].mode()[0]])


    # display the most common day of week
    print('Most common week day:',DAY_NA[data['week day'].mode()[0]])


    # display the most common start hour
    print('Most common hour:',data['hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
time_stats(data)

def station_stats(data):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('Most commonly used start station',data['Start Station'].value_counts().index[0])

    # display most commonly used end station
    print('Most commonly used end station',data['End Station'].value_counts().index[0])


    # display most frequent combination of start station and end station trip
    Frequent=data.groupby(['Start Station','End Station'])
    most_freq=Frequent.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of start station and end station trip',most_freq)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
station_stats(data)

def trip_duration_stats(data):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time',data['Trip Duration'].sum())

    # display mean travel time
    print('Mean travel time',data['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
trip_duration_stats(data)

def user_stats(data):
    """Displays statistics on bikeshare users."""
    if x[0]!= 'washington':

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        print('Counts of user types',data['User Type'].value_counts())
     
        # Display counts of gender
        print('Counts of gender',data['Gender'].value_counts())


        # Display earliest, most recent, and most common year of birth
        print('Earliest year of birth',data['Birth Year'].min())
        print('Most recent year of birth',data['Birth Year'].max())
        print('Most common year of birth',data['Birth Year'].mode()[0])


        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
user_stats(data)
view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
start_loc = 0
while view_data=='yes':
  print(data.iloc[start_loc:start_loc+5])
  start_loc += 5
  view_data = input("Do you wish to continue?: ").lower()
while True:
    restart = input('\nWould you like to restart? Enter yes or no.\n')
    if restart.lower() != 'yes':
        break
    else:
        sys.stdout.flush()
        os.execv(sys.argv[0], sys.argv)
