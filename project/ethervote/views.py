# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from ethervote.election import Election
from ethervote.serializers import ElectionSerializer


# Create your views here

@csrf_exempt
def election_list(request):
	if request.method == 'GET':
		election = Election()
		serializer = ElectionSerializer(election)
		return JsonResponse(serializer.data, safe=False)
