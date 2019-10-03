from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from home.analyzer import analyze
from django.contrib.auth import authenticate, login
import json

# Create your views here.
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect, requires_csrf_token, csrf_exempt


@csrf_exempt
def testresult(request):
	context =  {}
	if request.method == 'POST' :
		entity = request.POST['selected-entity']
		positive = 5885
		data = analyze(entity)
		print(data["counter"])

		context.update({"entity": entity})
		context.update({"facebook": data["facebook"]})
		context.update({"youtube": data["youtube"]})

		context.update({"positive": data["positive"]})

		context.update({"negative": data["negative"]})

		context.update({"neg1": data["neg1"]})
		context.update({"neg2": data["neg2"]})
		context.update({"neg3": data["neg3"]})
		context.update({"neg4": data["neg4"]})
		context.update({"neg5": data["neg5"]})
		context.update({"pos1": data["pos1"]})
		context.update({"pos2": data["pos2"]})
		context.update({"pos3": data["pos3"]})
		context.update({"pos4": data["pos4"]})
		context.update({"pos5": data["pos5"]})
		context.update({"rows": json.dumps(data["rows"])})
		print(data["rows"])

		context.update({"counter": data["counter"]})
		return render(request, "result.html", context)
	return redirect('')

@csrf_exempt
def home(request):
	template = loader.get_template('home.html')
	return HttpResponse(template.render())


@csrf_exempt
def aboutus(request):
	template = loader.get_template('aboutus.html')
	return HttpResponse(template.render())
