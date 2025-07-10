"""
URL configuration for Vocabloom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from VocabloomApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('courses/', courses),
    path('course/', course),
    path('contact/', contact),
    path('about/', about),
    path('blog/', blog),
    path('blog_single/', blog_single),
    path('login/', login),
    path('sign_up/', sign_up),
    path('lesson/', lesson),

    #text_to_speech
    path('word/', word),
    path('text_to_speech/', text_to_speech),
    path('pronounce/<str:word>/', gtts, name='text_to_speech'),
    #speech_to_text
    # path('speech/', speech),
    # path('speech_to_text/', speech_to_text),

    #certificate
    path('certificate/', certificate),

    #flash_card
    path('flash_card/', flash_card2),
    path('quiz/', quiz),
    path('mcq/', multiplechoice),
    path('calendar/', calendar),

    #speaking topics
    path('speaking_topics/', speaking_topics),
]
