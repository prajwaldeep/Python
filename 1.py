def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating
    
def convert_to_numeric(score):
    return int(score)
    
def sum_of_middle_three(a,b,c,d,e):
    score = [a,b,c,d,e]
    sum_of_middle_three = sum(score) - min(score) - max(score)
    return sum_of_middle_three
    
def score_to_rating_string(score):
    if 0 <= score < 1:
        rating = 'Terrible'
    elif 1 <= score < 2:
        rating = 'Bad'
    elif 2 <= score < 3:
        rating = 'OK'
    elif 3 <= score < 4:
        rating = 'Good'
    elif 4 <= score < 5:
        rating = 'Excellent'
    return rating

print(scores_to_rating(3,4,4,4,4))
 
