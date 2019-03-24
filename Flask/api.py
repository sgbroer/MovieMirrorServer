#import pickle

#rec_dict =  pickle.load(open('./Recommender/rec_dict.pkl', 'rb'))

from bs4 import BeautifulSoup
import requests
from numpy import random

url = 'https://www.zurinstitute.com/movie-therapy/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html5lib')

def get_movies(soup):
    return_list = []
    list_1 = soup.find('div', class_="col2blue-left")
    
    list_2 = categories_movies_2 = soup.find('div', class_="col2blue-right")

    
    return_list.append(list_1.contents[1])
    return_list.append(list_2.contents[1])
        
    return return_list

def build_dict(list_of_movie_lists):
    #Create dictionary
    return_dict = {}
    
    #Loop through each list object
    for movie_list in list_of_movie_lists:
        #Loop through children of list object
        for child in movie_list.children:
            
            #Build a list for each category
            movie_list = []
            #Check to make sure 
            if str(type(child)) == "<class 'bs4.element.Tag'>":
    
                category = child.find('span').text[:-1]     
                #print(category)
                for movie in child.contents:
                    #Leaving out <br> and category names
                    if "<" not in str(movie) and str(movie) != ", " and "\xa0" not in str(movie):
                        movie_list.append(movie)

                return_dict[category] = movie_list
    
    return return_dict

movies_soup_list = get_movies(soup)
built_dict = build_dict(movies_soup_list)

consolidate_dict = {

'Family Issues' : [
'Authority',
'Childhood Obesity',
'Abuse and Childhood Trauma',
'Domestic Violence and Rape',
],
 
'Addiction' : ['Addictions'],
 
'Emotions' : [
'Aging & End of Life',
'Anger and Forgiveness',
'Aspiration',
'Courage & Determination',
'Grief, Loss, Death & Transformation',
'Willpower',
'Stress Management',
'Risk',
'Sacrifice',
'Self-Esteem'],
 
'Spirituality' : [
'Authentic Self',
'Dreams, Inner Guidance, Intuition',
'Existential',
'Human Spirit, Hope & Inspiration',
'Pace of Life',
'Spirituality and Spiritual Awareness',
'Spirituality and Religion'],
 
'Trauma' : [
'Hearing Loss – Deafness',
'Post-Traumatic Growth',
'Sexual Abuse',
'Trauma'],
 
 
'Phobias' : [
'Phobias'],
 
'Attachment' : [
'Attachment-Disorganized',
'Attachment-Insecure',
'Attachment – Many Types',
'Attachment-Reactive',
'Attachment and Trauma'],
 
'Mental Condition' : [
'Autism',
'Bipolar',
'Depression',
'Dissociative Disorders',
'Eating Disorders',
'Intellectual Disability',
'OCD',
'PTSD',
'Schizophrenia'],
 
'Relationships' : [
'Separation & Divorce',
'LGBT',
'Relationships, Non-Traditional',
'Relationships, Online',
'Relationships & Love',
'Sexuality'],
 
'Body' : [
'Body Image'],
 
'Work' : [
'Vocational Issues',
'Retirement'],
 
'Social Problems' : [
'Consumerism',
'War (Horrors of and Aftermath)',
'Prejudice (coping with)',
'Psych. of Modern Tech-Digital Age',
'Social Justice']
}

rec_dict = {}

for key in consolidate_dict.keys():
    rec_dict[key] = []
    for consolidated_key in consolidate_dict[key]:
        rec_dict[key].extend(built_dict[consolidated_key])


example = {
  'Problem Area' : 'Abuse and Childhood Trauma'
}


def make_recommendation(features):
    
    result_list = rec_dict[features['Problem Area']]
    result = result_list[random.randint(0, len(result_list))]
    return result

if __name__ == '__main__':
    print(make_prediction(example))
