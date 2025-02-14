import operator 
def create_movie(movie_title,genre,rating):
    movie_dict={
        "title": " ",
        "genre": " ",
        "rating":0.0
    }
    if movie_title and genre and rating:
        # for movie in movie_title:
        #     movie_dict["title"]=movie
        # for kind in genre:
        #     movie_dict["genre"]=kind
        # for score in rating:
        #     movie_dict["rating"]=score
        movie_dict["title"]=movie_title
        movie_dict["genre"]=genre
        movie_dict["rating"]=rating
        return movie_dict
    else:
        return None



def add_to_watched(user_data, movie):
    user_data["watched"] += [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"] += [movie]
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data


def get_watched_avg_rating(user_data):
    ratings=[]
    average_rating=0
    if len(user_data["watched"]) == 0:
            average_rating=0.0
            return average_rating
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
        
    average_rating = sum(ratings) / len(ratings)
    return average_rating



def get_most_watched_genre(user_data):
    most_frequent_genre_list=[]
    most_common=None
    for movie in user_data["watched"]:
        
        most_frequent_genre_list.append(movie["genre"])
        most_common=max(most_frequent_genre_list, key=most_frequent_genre_list.count)
        print(most_frequent_genre_list)
    return most_common
    




#wave3
def get_unique_watched(user_data):
    unique_list=[]
    watched_friend_movie_list=[]
    user_watched_movie_list=[]
    for friend in user_data["friends"]:
        for movie in friend ["watched"]:
            watched_friend_movie_list.append(movie)

    for movie in user_data["watched"]:
        user_watched_movie_list.append(movie)

    for movie in user_watched_movie_list:
        
        if movie not in watched_friend_movie_list:
            unique_list.append(movie)
    return unique_list

def get_friends_unique_watched(user_data):
    unique_list_doop=[]
    unique_list=[]
    watched_friend_movie_list=[]
    user_watched_movie_list=[]
    for friend in user_data["friends"]:
        for movie in friend ["watched"]:
            watched_friend_movie_list.append(movie)

    for movie in user_data["watched"]:
        user_watched_movie_list.append(movie)

    for movie in watched_friend_movie_list:
        if movie not in user_watched_movie_list:
            unique_list_doop.append(movie)
    
    for movie in unique_list_doop:
        if movie not in unique_list:
            unique_list.append(movie)
    return unique_list
    
