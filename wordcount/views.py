from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
	return render(request,'home.html')



def eggs(request):
	return HttpResponse("This is an egg page.")

def count(request):
	Fulltext= request.GET['Fulltext']
	words = Fulltext.split()
	worddict = {}

	for word in words:
		if word in worddict:
			worddict[word]+=1 
		else:

			worddict[word]=1


	check = worddict.items()
	final = sorted ( check , key = lambda x : x[1], reverse=True)		
	length = len(words)
	return render(request , 'count.html', {'text' : Fulltext, 'length' : length, "worddict":final} )


def about(request):
	return render ( request, 'about.html')