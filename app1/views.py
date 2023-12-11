from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .models import Products

# Create your views here.

def add_movies(request):
    movie_details={
        'movies':[
        {
        'title':'GODFATGHER',
        'year':1990,
        'summary':'The story is of "Ithakk" and his friend Jonnappan, petty thieves, Jonnappans disappearance, Ithakk taking care of his friends family .',
        'image_url':'https://files.prokerala.com/movies/pics/800/godfather-first-look-posters-100854.jpg'
    },
    {
        'title':'TITANIC',
        'year':2004,
        'summary':' based on accounts of the sinking of RMS Titanic in 1912. Kate Winslet and Leonardo DiCaprio star as members of different social classes who fall in love during the ships maiden voyage.',
         'image_url':'https://m.media-amazon.com/images/I/610CYrdV7AS.jpg'
    },
    {
        'title':'KAATHAL',
        'year':2023,
        'summary':'Mathew Devassy wife Omana,How Mathew accepts the divorce case and overcomes his struggle with his sexuality forms the crux of the film. ',
         'image_url':'https://m.media-amazon.com/images/M/MV5BOGYxY2MyZDAtOTU5ZS00OWUyLTg5YWItNDViMGRkNGQ5MWZhXkEyXkFqcGdeQXVyMjkxNzQ1NDI@._V1_.jpg'
    },
    {
        'title':'AANANDHAM',
        'year':2020,
        'summary':'Seven friends visit Goa and Hampi while on their college trip. Their experiences during their journey help them understand the intricacies of love and friendship.',
         'image_url':'https://mir-s3-cdn-cf.behance.net/project_modules/hd/6fea0945574525.5835889a6dcaa.jpg'
    }
    
    ]}
    return render(request,'index.html',movie_details)

    
def student_list(request):
    count=request.session.get('count',0)
    print(request.COOKIES)
    count=int(count)
    count=count+1
    request.session['count']=count
    students=Student.objects.all()
    response=render(request,'student.html',{'students':students,'visits':count})
    return response

def index(request):
    products=Products.objects.all()
    return render(request,'products.html',{'products':products})