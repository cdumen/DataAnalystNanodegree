## TODO: import all necessary packages and functions
import csv
import datetime
import sys
import numpy as np
import pandas as pd
import time
import calendar
import os


#from IPython.display import display
chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'

def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
   # TODO: handle raw input and complete function

    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    global city_file
    if city.lower() == "chicago":
        print('\nCity: {}'.format(city))
        city_file = chicago
        return city_file
   
    elif city.lower()=="new york":
        print('\nCity: {}'.format(city))
        city_file=new_york_city
        return city_file
    elif city.lower()=="washington":
        print ('\nCity: {}'.format(city))
        city_file=washington
        return city_file
    else:
        print('Invalid Input, Try again')
        return get_city() 
    return city_file

def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: string time period to filter data
    '''
    global time_period
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
                  
    # TODO: handle raw input and complete function
    #from get_city import city
    #city=get_city()
    if time_period=='month':
        month=get_month()
    elif time_period=='day' :
        day=get_day()
    elif time_period=='none':
        print('No Filter Needed')
    else:
        
        print('Invalid Input, Try again')
        return get_time_period()
    return time_period
    
def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: string month data to filter months
    '''
    global month
    month = input('\nWhich month? January, February, March, April, May, or June?\n')
    month=[month]
    # TODO: handle raw input and complete function
    return month
def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: special day to filter data
    '''
    global day
    day = str(input('\nWhich day? Please type your response as an integer.\n'))
    day=[day]
    return day

def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Arguments:city_file, time_period
    Returns: popular month string
    Question: What is the most popular month for start time?
    ''' 
    popular_month=df_n['start_month'].value_counts().idxmax()
    print("popular month is: ",popular_month)
    # TODO: complete function
def get_city_file():
    global df_n
    df=pd.read_csv(city_file)
    trip_date = df['Start Time'].apply(lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))
#   df.to_csv(city_file)
    if time_period=='month':
        df['start_month'] = trip_date.apply(lambda x: x.strftime("%B"))
        df['start_day']  = trip_date.apply(lambda x: x.strftime("%A"))
        df['start_hour']  = trip_date.apply(lambda x: x.strftime('%H'))
        df_n = df.loc[df['start_month'].isin(month)]
#        print(df_n.head())
        return df_n
    elif time_period=='day':
        df['start_day']  = trip_date.apply(lambda x: x.strftime('%d'))
        df['start_day'] = df['start_day'].map(lambda x: x.lstrip('0'))
        df['start_hour']  = trip_date.apply(lambda x: x.strftime('%H'))
        df_n = df.loc[df['start_day'].isin(day)]
        return df_n
    elif time_period == 'none':
        df['start_month'] = trip_date.apply(lambda x: x.strftime("%B"))
        df['start_day']  = trip_date.apply(lambda x: x.strftime("%A"))
        df['start_hour']  = trip_date.apply(lambda x: x.strftime('%H'))
        df_n=df
        return df_n
    # TODO: complete function

def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Arguments:city_file, time_period
    Returns: popular day string
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function  
    popular_day=df_n['start_day'].value_counts().idxmax()
    print("popular day is: ",popular_day)

    # TODO: complete function

def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Arguments:city_file, time_period
    Returns: popular hour
    Question: What is the most popular hour of day for start time?
    '''

    popular_hour=df_n['start_hour'].value_counts().idxmax()
    print("popular hour is: ",popular_hour)

def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Arguments: city file, time period
    Returns: trip duration
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    # Create dataframe
    
    total=np.sum(df_n['Trip Duration'])
    average = np.average(df_n['Trip Duration'])
    d = total // (24 * 60 * 60)
    total %= (24 * 60 * 60)
    h = total // (60 * 60)
    total %= (60 * 60)
    m = total // 60
    s = total % 60
    d1 = average // (24 * 60 * 60)
    average %= (24 * 60 * 60)
    h1 = average // (60 * 60)
    average %= (60 * 60)
    m1 = average // 60
    s1 = average % 60   
    print('Average trip {:n} days, {:n} hours, {:n} minutes, {:n} seconds'.format(d1, h1, m1, s1))
    print('Total trip {:n} days, {:n} hours, {:n} minutes, {:n} seconds'.format(d, h, m, s))
    # Calculate average

    return(average, total)

def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Arguments: city file, time period
    Returns: popular start station and popular end station
    Question: What is the most popular start station and most popular end station?
    '''
#    # TODO: complete function


    popular_start=df_n['Start Station'].value_counts().idxmax()
    popular_end=df_n['End Station'].value_counts().idxmax()
    print("popular start station is: ", popular_start)
    print("popular end station is: ", popular_end)
    # Calculate average
 
def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Arguments: city file, time period
    Returns: popular trip which start station to end station trip is used.
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    trip = df_n.groupby(["Start Station", "End Station"]).size().reset_index(name="Time")
    trip1=trip.sort_values(by=['Time'])
    most_used = trip1['Start Station'][trip1.index[-1]]
    most_used2 = trip1['End Station'][trip1.index[-1]]
    print("popular trip is: {} to {}".format(most_used, most_used2))

def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Arguments: city file, time period
    Returns: numbers of user type suscribers and customers
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    n_subscribers = len(df_n[df_n['User Type']=='Subscriber'])
    n_customers = len(df_n[df_n['User Type']=='Customer'])
    n_total = n_subscribers + n_customers
    print("number of subscribers: ", n_subscribers)
    print("number of customers: ", n_customers)
    print("total users: ", n_total)   
    
    return(n_subscribers, n_customers, n_total)


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Arguments: city file, time period
    Returns: Number of females and males
    Question: What are the counts of gender?
    '''
    # TODO: complete functiono
    
    n_female = len(df_n[df_n['Gender']=='Female'])
    n_male = len(df_n[df_n['Gender']=='Male'])
    n_gender= n_female + n_male
    print("female users: ", n_female)
    print("male users: ", n_male)
    print("all genders:", n_gender) 
    return(n_female,n_male,n_gender) 


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Arguments: city file, time period
    Returns: popular birth years among all users
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    # TODO: complete function

    df2 = df_n[np.isfinite(df_n['Birth Year'])]  
    birthday =df2.sort_values(by=['Birth Year']) 
    older = birthday['Birth Year'][birthday.index[0]]  
    younger = birthday['Birth Year'][birthday.index[-1]]
    popular=df2['Birth Year'].value_counts().idxmax()
    print("popular birth year is: ",popular)
    print("older person birth year is: ",older)
    print("younger person birth year is: ",younger)  
    return(older,younger,popular)
    
 
def display_data():
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
        returns city file first 5 entry if needed from user it displays five more
    
    '''
#    df1=pd.read_csv(city_file)
#    print(df1.head())
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function
    i = 0
    while (i>=0):
        if (display == 'yes'):
                i += 5
                print(df_n.head(i))
                display = input('\nWould you like to view individual trip data?'
                        ' Type \'yes\' or \'no\'.\n')

        if ( display == 'no'):
            i = -1
            return
def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()

    # Filter by time period (month, day, none)
    time_period = get_time_period()
    df = get_city_file()

    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = time.time()
        
        #TODO: call popular_month function and print the results
        popular_month(city,time_period)
        
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none' or time_period == 'month':
        start_time = time.time()
        
        # TODO: call popular_day function and print the results
        popular_day(city_file,time_period)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")    

    start_time = time.time()

    # What is the most popular hour of day for start time?
    # TODO: call popular_hour function and print the results
#    popular_hour(city_file,time_period)
    popular_hour(city_file,time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the total trip duration and average trip duration?
    # TODO: call trip_duration function and print the results
    trip_duration(city_file, time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()
    

    # What is the most popular start station and most popular end station?
    # TODO: call popular_stations function and print the results
#    popular_stations(city_file,time_period)
    popular_stations(city_file,time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
    popular_trip(city_file,time_period)
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of each user type?
    # TODO: call users function and print the results
    users(city_file,time_period)
    
    print("That took %s seconds." % (time.time() - start_time))
    print("Calculating the next statistic...")
    start_time = time.time()

    # What are the counts of gender?
    # TODO: call gender function and print the results
    if city_file == chicago or city_file == new_york_city:
        start_time = time.time()
        gender(city_file,time_period)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
    start_time = time.time()

    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
    # TODO: call birth_years function and print the results
    if city_file == chicago or city_file == new_york_city:
        start_time = time.time()
        birth_years(city_file,time_period)
        print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data()

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
	statistics()