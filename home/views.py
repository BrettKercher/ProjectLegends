from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .forms import SummonerNameForm
from .helpers import *

import os
import requests
 
API_KEY = os.environ['RIOT_API_KEY']

def index(request):
	if request.method == 'POST':
		form = SummonerNameForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['summoner_name']
			region = form.cleaned_data['region']

			baseUrl = 'https://na.api.pvp.net'
			summonerUrl = getSummonerUrl(region, name)

			params = { 'api_key': API_KEY }

			r = requests.get(baseUrl + summonerUrl, params=params)
			payload = r.json()

			summonerID = payload[name.lower().replace (' ', '')]['id']

			matchUrl = getMatchUrl(region, summonerID)
			r = requests.get(baseUrl + matchUrl, params=params)
			payload = r.json()

			print(payload)


			return HttpResponseRedirect(reverse('polls:index'))
	else:
		form = SummonerNameForm(initial={'region':'NA'})

	return render(request, 'home/index.html', {'form': form})