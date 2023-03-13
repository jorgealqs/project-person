from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import os
import openai

# Create your views here.


class chatgtp(View):
    def get(self, request) -> HttpResponse:
        # openai.api_key = "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"
        # response = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=[
        #         {"role": "user", "content": "help me please?"}
        #     ]
        # )
        # print(f"\n\n\n{response} {type(response)}\n\n\n")
        return render(request, "chatgpt.html", {})
