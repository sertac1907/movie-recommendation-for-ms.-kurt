import streamlit as st
import time 
import random

import base64
def get_movies(path):
    with open(path,"r") as file:
        movies = file.readlines()
    return movies

def write_movies(local_movies,path):
    with open(path,"w") as file:        
        file.writelines(local_movies)


def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )










st.set_page_config("Movie List",layout="wide")

col1, col2 =st.columns([15,5]) 

movies = get_movies("movie_list/movies.txt")
watched_movies = get_movies("movie_list/watched_movies.txt")

with col1:

    st.title("Movies That Kandemir Suggested")

    for index,movie in enumerate(movies):

        check = st.checkbox(movie,key=movie)
        if check:
            number = random.randrange(4,7)
            time.sleep(0.1)
            autoplay_audio(f"C:/Users/Sertac/Documents/GitHub/Movie-Recommendation-For-Ms.-Kurt/movie_list/sound_effects/{number}.mp3")
            time.sleep(4)
            
            movies.pop(index)
            write_movies(movies,"movie_list/movies.txt")
            del st.session_state[movie]

            watched_movies.append(movie)
            write_movies(watched_movies,"movie_list/watched_movies.txt")
            st.rerun()
    
            
    st.title("Movies That Kurt Watched")

    for movie in watched_movies:
        invisible_check = st.checkbox(movie,key=movie,value=True)
        


        
  
    
    


with col2:
    with st.empty():
        while 1:
            clock = time.strftime("""%H:%M:%S
                                  %d.%m.%Y""")
            st.write(clock)
            time.sleep(1)
   
     
        
        
st.session_state