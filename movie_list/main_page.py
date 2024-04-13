import streamlit as st
import time 

def get_movies(path):
    with open(path,"r") as file:
        movies = file.readlines()
    return movies

def write_movies(local_movies,path):
    with open(path,"w") as file:        
        file.writelines(local_movies)






st.set_page_config("Movie List",layout="wide")

col1, col2 =st.columns([15,5]) 

movies = get_movies("PyhtonMegaCourse/Streamlit/movie_list/movies.txt")
watched_movies = get_movies("PyhtonMegaCourse/Streamlit/movie_list/watched_movies.txt")

with col1:

    st.title("Movies That Kandemir Suggested")

    for index,movie in enumerate(movies):

        check = st.checkbox(movie,key=movie)
        if check:
            
            movies.pop(index)
            write_movies(movies,"PyhtonMegaCourse/Streamlit/movie_list/movies.txt")
            del st.session_state[movie]

            watched_movies.append(movie)
            write_movies(watched_movies,"PyhtonMegaCourse/Streamlit/movie_list/watched_movies.txt")
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

        
        
        
#st.session_state