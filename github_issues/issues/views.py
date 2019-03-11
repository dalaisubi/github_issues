from django.shortcuts import render
import requests

from github_issues.utils import validate_web_url

# Create your views here.



def issuesView(request):

    """A view of all issues of user provided public git repo."""

    url = request.GET.get('url', None)
    is_url = None
    response = None
    try: 
    	is_url = validate_web_url(url)
    except:
    	print("this is not a url")
    	is_url = False	

    if is_url:
    	url_split = url.split('/')
    	total_open_issues = requests.get('https://api.github.com/repos/{}/{}'.format(url_split[-2], url_split[-1])).json()['open_issues']	
    	
    	page_no = 0
    	while(True):
    		response = requests.get("https://api.github.com/repos/"+url_split[-2]+"/"+url_split[-1]+"?page="+str(page_no)).json()
    		if len(response) > 0:
    			print("https://api.github.com/repos/"+url_split[-2]+"/"+url_split[-1]+"?page="+str(page_no))
    			print( response,'-----')
    			page_no += 1
    		else:
    			break		    
    print(len(response.json()))
    context = {
    	"git_api" : 'https://api.github.com/repos/{}/{}'.format(url.split('/')[-2], url.split('/')[-1]),
    	"response": response.json()
    }	
    return render(request, 'index.html', context)	