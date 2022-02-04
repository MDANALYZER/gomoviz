import streamlit as st
import pickle
import requests

st.set_page_config(page_title="GoMoviz", page_icon=":movie_camera:", layout="centered")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")   

def fetch_poster(id):
    
    url = "https://api.themoviedb.org/3/movie/{}?api_key=72ddcc9f90608ff386ae227d1b471366&language=en-US".format(id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path 

def movie_details(id):
    st.write('####')
    with st.container():
        left, right = st.columns(2)
        with left:
           poster =  fetch_poster(id)
           st.image(poster)
        with right:
            url = "https://api.themoviedb.org/3/movie/{}?api_key=72ddcc9f90608ff386ae227d1b471366&language=en-US".format(id)
            data = requests.get(url)
            data = data.json()  
            genres = data['genres'] 
            rating = data['vote_average']
            title = data['original_title']
            runtime = data['runtime']
            homepage = data['homepage']
            status = data['status']
            date = data['release_date']

            s=[]
            for i in genres:
                s.append(i['name'])
                genre = ' '.join(str(ele) for ele in s)
            st.subheader(title)
            st.text(genre)
            st.write('####')
            st.write('####')
            st.write('####')
            st.text('Ratings: {}'.format(rating))
            st.text('Status: {}'.format(status))
            st.text('Date: {}'.format(date))
            st.text('Runtime: {}'.format(runtime))
            
        
        st.write('---')
        st.write('##')
def trend_details(id):
    poster = fetch_poster(id)
    url = "https://api.themoviedb.org/3/movie/{}?api_key=72ddcc9f90608ff386ae227d1b471366&language=en-US".format(id)
    data = requests.get(url)
    data = data.json() 
    title = data['original_title']
    st.text(title)
    st.image(poster)


#----Side Bar Funtion. category Selector-----#

st.sidebar.title('Search By Category')
category = st.sidebar.selectbox('Selet Category',['Home','Action Adventure','Comedy Family','Horror Thriller'])

#----Action/Adventure Section------#
if category=='Action Adventure':
    aa_movie = pickle.load(open('aa.pkl','rb'))
    aa_list = aa_movie['title'].values
    row = int(len(aa_movie)/4)
    index = 0
    i = 0

    for i in range(row):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            name = aa_list[index]
            st.text(name)
            id = aa_movie[aa_movie['title']==name].movie_id.values
            poster = fetch_poster(id[0])
            st.image(poster)
            index = index+1

            
        with col2:
            name = aa_list[index]
            st.text(name)
            id = aa_movie[aa_movie['title']==name].movie_id.values
            poster = fetch_poster(id[0])
            st.image(poster)
            index = index+1
        
        with col3:
            name = aa_list[index]
            st.text(name)
            id = aa_movie[aa_movie['title']==name].movie_id.values
            poster = fetch_poster(id[0])
            st.image(poster)
            index = index+1
        
        with col4:
            name = aa_list[index]
            st.text(name)
            id = aa_movie[aa_movie['title']==name].movie_id.values
            poster = fetch_poster(id[0])
            st.image(poster)
            index = index+1
   


#-------Comedy/Family Section-----#

if category=='Comedy Family':
    cm_movie = pickle.load(open('cm.pkl','rb'))
    cm_list = cm_movie['title'].values
    row = int(len(cm_movie)/4)
    index = 0

    for i in range(row):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            name = cm_list[index]
            st.text(name)
            id = cm_movie[cm_movie['title']==name].movie_id.values
            poster = fetch_poster(id[0])
            st.image(poster)
            index = index+1
        
        with col2:
            name = cm_list[index]
            st.text(name)
            id = cm_movie[cm_movie['title']==name].movie_id.values
            poster = fetch_poster(id[0])
            st.image(poster)
            index = index+1
        
        with col3:
            name = cm_list[index]
            st.text(name)
            id = cm_movie[cm_movie['title']==name].movie_id.values
            poster = fetch_poster(id[0])
            st.image(poster)
            index = index+1
        
        with col4:
            name = cm_list[index]
            st.text(name)
            id = cm_movie[cm_movie['title']==name].movie_id.values
            poster = fetch_poster(id[0])
            st.image(poster)
            index = index+1    
   

if category=='Horror Thriller':
    th_movie = pickle.load(open('th.pkl','rb'))
    th_list = th_movie['title'].values
    row = int(len(th_movie)/4)
    index = 0

    for i in range(row):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            name = th_list[index]
            st.text(name)
            id = th_movie[th_movie['title']==name].movie_id.values
            poster = fetch_poster(id[0])
            st.image(poster)
            index = index+1
        
        with col2:
            name = th_list[index]
            st.text(name)
            id = th_movie[th_movie['title']==name].movie_id.values
            poster = fetch_poster(id[0])
            st.image(poster)
            index = index+1
        
        with col3:
            name = th_list[index]
            st.text(name)
            id = th_movie[th_movie['title']==name].movie_id.values
            poster = fetch_poster(id[0])
            st.image(poster)
            index = index+1
        
        with col4:
            name = th_list[index]
            st.text(name)
            id = th_movie[th_movie['title']==name].movie_id.values
            poster = fetch_poster(id[0])
            st.image(poster)
            index = index+1    
        

contact_form = """
    <form action="https://formsubmit.co/dashmadhusudan@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
st.sidebar.markdown(contact_form, unsafe_allow_html=True)
    
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:9]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters


st.header('GOMOVIZ')
movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
 
    id = movies[movies['title']==selected_movie].movie_id.values
    movie_details(id[0])


    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    st.write('####')
    col5, col6, col7, col8 = st.columns(4)   
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])
    with col7:
        st.text(recommended_movie_names[6])
        st.image(recommended_movie_posters[6])
    with col8:
        st.text(recommended_movie_names[7])
        st.image(recommended_movie_posters[7])        
st.write('####')
st.write('####')
st.write('####')
st.subheader('Trending movies')
st.write('####')
trend = pickle.load(open('trend.pkl','rb'))
trend_list = trend['Id'].values
index = 0

for i in range(2):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        id = trend_list[index]
        trend_details(id)
        index = index + 1
        
    with col2:
        id = trend_list[index]
        trend_details(id)
        index = index + 1
        
    with col3:
        id = trend_list[index]
        trend_details(id)
        index = index + 1
        
    with col4:
        id = trend_list[index]
        trend_details(id)
        index = index + 1
    st.write('####')    