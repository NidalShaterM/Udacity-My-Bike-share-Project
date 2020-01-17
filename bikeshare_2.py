import pandas as pd

raw = {'chicago': 'chicago.csv','new york city': 'new_york_city.csv', 'washington': 'washington.csv'}

def get_from_files(city, month, day):
    df = pd.read_csv(raw[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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

def choices():
    city = test_string("Choose a City chicago, new york city or washington?", 'a')
    month = test_string("Choose a month  january, ... june or all", 'b')
    day = test_string("Choose a day monday, tuesday, ... sunday or all", 'c')
    return city, month, day

def test_string(user_str,type):
    #The user can retry one hadered times until correct
    for x in range(100):
        result_str=input(user_str).lower()
        try:
            if type == 'a' and result_str in ['chicago','new york city','washington']:
                break
            elif type == 'b' and result_str in ['all','january', 'february', 'march', 'april', 'may', 'june']:
                break
            elif type == 'c' and result_str in ['all','sunday','monday','tuesday','wednesday','thursday','friday','saturday']:
                break
            else:
                if type == 'a':
                    print("Valid: chicago new york city or washington")
                if type == 'b':
                    print("Valid: january, february, march, april, may, june or all")
                if type == 'c':
                    print("Valid: sunday, ... friday, saturday or all")
        except ValueError:
            print("Sorry, your input is wrong")
    return result_str




def get_stats(df,city):
    print('\nCalculating The Most Frequent Times of Travel...\n')

    # display the most common month
    most_common_month = df['month'].mode()[0]

    print('Most Popular Month:', most_common_month)

    # display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]

    print('Most Day Of Week:',  most_common_day_of_week)

    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]

    print('Most Common Start Hour:',  most_common_start_hour)

    print('\nCalculating The Most Popular Stations and Trip...\n')

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]

    print('Most Start Station:', most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]

    print('Most End Station:',  most_common_end_station)

    # display most frequent combination of start station and end station trip
    group_of_start_end = df.groupby(['Start Station', 'End Station'])
    most_common_combination_station = group_of_start_end.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', most_common_combination_station)

    print('\nCalculating Trip Duration...\n')

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()

    print('Total Travel Time:', total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()

    print('Mean Travel Time:', mean_travel_time)

    print('\nCalculating User Stats...\n')
    # Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:', most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:', most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:', earliest_year)
def main():
    pd.set_option('display.max_columns', None)
    # The user can replay the program 100 times
    for x in range(100):
        city, month, day = choices()
        df = get_from_files(city, month, day)

        get_stats(df,city)
        rows=0;
        # The user can replay this option 100 times
        for x in range(100):
            print(df[rows:rows + 5])
            more_rows = input('\nMore individual trips? (yes/no).\n')
            rows=rows+5
            if more_rows.lower() != 'yes':
                break
        restart = input('\nRestart? (yes/no).\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()


