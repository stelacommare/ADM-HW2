from collections import Counter
from datetime import datetime as dt
import numpy as np

def posts_by_interval(intervals, datetimes):

    # initializing an array with all 0: the i-th element of the array represents a counter of the posts published during the i-th time interval in input
    result = np.zeros(len(intervals), dtype = np.int32)

    
    # converting the elements of the list 'intervals' in time objects
    intervals = [(dt.strptime(i[0], '%H:%M:%S').time(),(dt.strptime(i[1], '%H:%M:%S').time())) for i in intervals]

    # starting a counter of times that a certain time compares in the datetime serie 
    counter = Counter(datetimes)


    # iterating over the grouped times of publication in counter in order to increment the value of the elements in the 'result' array
    for time in counter:
        for interval, i in zip(intervals, range(len(intervals))):
            if time >= interval[0] and time <= interval[1]:
                result[i] += counter[time]
                break
    return result



def posts_hist(datetimes, time_intervals):
    counter = defaultdict(int)
    # initializing a counter for each time interval in the list
    counter = {key:0 for key in time_intervals}
    for item in datetimes.iteritems():
        for key in list(counter.keys()):
            left_end, right_end = key.split(" ")
            left = dt.strptime(left_end, '%H:%M:%S').time()
            right = dt.strptime(right_end, '%H:%M:%S').time()
            if item[1] <= right and item[1] >= left:
                counter[key]+=1
                # we found the correct interval and we increment the counter in occurrence of that interval
                # in order to skip the next iterations we use break
                break
    plt.figure(figsize=(20, 8))
    plt.bar(list(counter.keys()), list(counter.values()))
    plt.show()
    for key in counter.keys():
        a, b = key.split()
        print(f'The number of posts published between {a} and {b} is {counter[key]}')




#the function posts_by_profileid returns the posts published by the user passed as argument

def posts_by_profileid(profile_id,posts):
    return posts[posts['profile_id']==profile_id]


# The function posts_by_profileid2 returns all the posts that are published by an user that is present in the list passed as argument
# the only difference from the funtion above is the argument passed: in this case is a list of profile ids

def posts_by_profileid2(profiles,posts):
    return posts[posts['profile_id'].isin(profiles)]



# Now the function influencers_posts takes in input an integer an returns all the posts of the most 'active' profiles
# thus we use a combination with the function decribed in the cells above

def influencers_posts(n,profiles,posts):
    # finding the n top posted profiles
    influencers = profiles.sort_values('n_posts',ascending=False)['profile_id'].head(n).tolist()
    return posts_by_profileid2(influencers,posts)
    


def influencers_posts2(n,profiles,posts):
    # finding the n top followed profiles
    influencers = profiles.sort_values('followers',ascending=False)['profile_id'].head(n).tolist()
    return posts_by_profileid2(influencers,posts)