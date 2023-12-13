"""You are given a list of dictionaries, where each dictionary represents a book and contains information about its 
title, authorand a list of reviews, where each review is a dictionary containing information about
thereviewer's name, rating, and comments. Write a function that 'takes in this list and returns the
 average rating for each book, along with  """                                                                                                                                                                     ' the total number of reviews for each book. If a book has no reviews, its average rating should be 0.


input_list = [    {        "title": "The Great Gatsby",        "author": "F. Scott Fitzgerald",        "reviews": [
    {"name": "John Doe", "rating": 4, "comments": "Great book!"},
    {"name": "Jane Smith", "rating": 3, "comments": "Good read."},
    {"name": "Bob Johnson", "rating": 5, "comments": "Amazing!"},        ]
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "reviews": [
            {"name": "Alice Chen", "rating": 4, "comments": "Very well-written."},
            {"name": "Tom Smith", "rating": 4, "comments": "Enjoyed reading it."},
        ]
    },
    {
        "title": "1984",
        "author": "George Orwell",
        "reviews": []
    }
]





def ave_ratings(input_list):
    result = []
    for i in input_list:
        print(i)
        total_ratings = 0
        total_reviews = len(i['reviews'])
        if total_reviews > 0:
            for review in i['reviews']:
                total_ratings += review['rating']
            average_rating = total_ratings / total_reviews
        else:
            average_rating = 0
        result.append({'title': i['title'], 'average_rating': average_rating, 'total_reviews': total_reviews})
    return result
print(ave_ratings(input_list))