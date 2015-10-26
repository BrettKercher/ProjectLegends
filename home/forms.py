from django import forms

class SummonerNameForm(forms.Form):
	CHOICES=[('NA', 'NA'),
			 ('EUW', 'EUW'),
			 ('EUNE', 'EUNE'),
			 ('BR', 'BR'),
			 ('TR', 'TR'),
			 ('RU', 'RU'),
			 ('LAN', 'LAN'),
			 ('LAS', 'LAS'),
			 ('OCE', 'OCE'),
	]
	summoner_name = forms.CharField(
	    				label='Summoner Name', 
	                    widget=forms.TextInput(attrs={'placeholder': 'Summoner Name'}),
	                    max_length=30,)
	region = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect,)