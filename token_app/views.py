from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Token
import secrets, random
from django.utils import timezone

def create(request):
    pool_capacity = 5
    my_dict = {'pool': pool_capacity}
    Token.objects.all().delete()
    for i in range(pool_capacity):
        Token(key=secrets.token_hex()).save()
    return render(request, 'token_app\create.html', context=my_dict)


def index(request):
    list_of_free_tokens = Token.objects.filter(state='Free')

    if len(list_of_free_tokens) == 0:
        raise Http404("No Tokens are Free in the pool currently, please come back after some time.")
    else:
        token_to_be_alloted = random.choice(list_of_free_tokens)
        token_to_be_alloted.state='Blocked'
        token_to_be_alloted.updated_at=timezone.now()
        token_to_be_alloted.save()
        my_dict = {'token_index': token_to_be_alloted.key}
        # blocked_alive(token_to_be_alloted.key,repeat=10)
        return render(request, 'token_app/index.html', context = my_dict)

def delete(request, token_key):
    Token.objects.filter(key=token_key).delete()
    Token(key=secrets.token_hex()).save()
    return render(request, 'token_app/delete.html',context={'token':token_key})

def end(request, token_key):
    token_end = Token.objects.filter(key=token_key).first()
    token_end.state='Free'
    token_end.updated_at=timezone.now()
    token_end.save()

    return render(request, 'token_app/end.html')


def is_alive(token_key):
    check_token = Token.objects.filter(key=token_key).first()
    check_token.last_alive=timezone.now()

# @background(schedule=10)
# def blocked_alive(token_key):
#     check_token = Token.objects.filter(key=token_key).first()
#     if ((timezone.now())-(check_token.last_alive)).seconds > 60:
#         print("Hello World!")
#         # return render(request, 'token_app/end.html')
