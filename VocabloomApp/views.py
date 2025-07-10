#flash card
import pandas as pd
import os

from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse


#sound
import pyttsx3
from gtts import gTTS

# Import pygame for playing the converted audio
import pygame

#word def
from wiktionaryparser import WiktionaryParser
from pydictionary import Dictionary

#speech to text
from google import genai
from google.genai import types

import speech_recognition as sr

# Create your views here.
def home(request):
    return render(request, 'index2.html')

def courses(request):
    return render(request, 'courses.html')

def course(request):
    return render(request, 'course.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog_single.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def sign_up(request):
    return render(request, 'sign_up.html')

def sign_up(request):
    return render(request, 'sign_up.html')


def lesson(request):
    return render(request, '_lesson.html')

### word sound testing ###
def word(request):
    return render(request, '_sound_test.html')


def text_to_speech(request):
    #user input
    word_list = request.POST.get('word')

    # print("Word to pronounce : ",word)
    
    # Initialize the Pyttsx3 engine
    engine = pyttsx3.init()
    
    # We can use file extension as mp3 and wav, both will work
    engine.save_to_file(word_list, 'static/media/speech.mp3')
    # engine.say(word)
    # Wait until above command is not finished.
    engine.runAndWait()
    # dict = Dictionary("song")
    # definition = dict.print_meanings()
    # print(definition)
    # return render(request, 'flash_card.html',{'definition': definition})
    return render(request, '_sound_test.html')
### end of sound test #####

#speech_to_text
def speech_to_text(request):
#pip install SpeechRecognition pyaudio

# Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Microphone as source
    # listening the speech and store in audio_text variable
    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        # recoginze_() method will throw a request
        # error if the API is unreachable,
        # hence using exception handling
        speech = r.recognize_google(audio_text)
        try:
            # using google speech recognition
            # r.recognize_google(audio_text,  language='my-MM')
            
            print("Text: "+ speech)
        except:
            print("Sorry, I did not get that")
    return JsonResponse({'speech': speech})
### end of sound test #####

### certificate ###
def certificate(request):
    return render(request, '_html2pdf.html', {'name': 'Thinn Thandar Zaw', 'Date': '12.6.2025'})

### flash card #####
def flash_card(request):
    csv_folder_path = os.path.join(settings.BASE_DIR, 'static', 'dataset')
    output_excel_path = os.path.join(settings.BASE_DIR, 'static', 'dataset', 'eg.xlsx')

    all_data = []  # List to collect DataFrames

    for csv_file in os.listdir(csv_folder_path):
        if csv_file.endswith('.csv'):
            file_path = os.path.join(csv_folder_path, csv_file)
            df = pd.read_csv(file_path)
            all_data.append(df)

    # Concatenate all DataFrames
    combined_df = pd.concat(all_data, ignore_index=True)

    # Write to one sheet
    combined_df.to_excel(output_excel_path, index=False)

    print(f"All CSV files have been combined into a single sheet in {output_excel_path}")

    #  for dictionary
    output_file_path = os.path.join('static', 'dataset', 'eg.xlsx')
    data = pd.read_excel(output_file_path)
    client = genai.Client(api_key="AIzaSyBeT1fp3_XDYC7djF7P4UEY6wtyiHJ19xw")
    df = pd.DataFrame(data['headword'])
    
    word_def = []
    a1_words_df = data[data['CEFR'] == 'A2']

    # Get a list of only the headwords for CEFR 'A1'
    a1_words = a1_words_df['headword'].tolist()

    # print(a1_words)

    for word in a1_words[:5]:
    #for word in df['headword'].head():
        defintion = f"suitable definition of {word} in english vocabulary,only definiton without examples,*"
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents = defintion,
        )
        american_pronunciation_prompt = f'give only american phonetic sign of {word}'
        american_pronunciation = client.models.generate_content(
            model="gemini-2.0-flash",
            contents= american_pronunciation_prompt,
        )
        british_pronunciation_prompt = f'give only american phonetic sign of {word}'
        british_pronunciation = client.models.generate_content(
            model="gemini-2.0-flash",
            contents= british_pronunciation_prompt,
        )
        
        word_def.append({
        'word': word,
        'definition': response.text,
        'american_pronunciation':american_pronunciation.text,
        'british_pronunciation':british_pronunciation.text,
        })
        

    return render(request, 'flash_card.html', {'word_def': word_def})
### end of flash card ###
def flash_card2(request):
    return render(request, 'flash_card.html')


def gtts(request, word):
    
    # Create a gTTS object
    tts = gTTS(text=word, lang='en')

    # Save the audio file
    audio_file = 'speech.mp3'
    tts.save(audio_file)

    # Initialize the mixer module
    pygame.mixer.init()

    # Load the mp3 file
    pygame.mixer.music.load("speech.mp3")

    # Play the loaded mp3 file
    pygame.mixer.music.play()
    # Return the path to the saved audio file
    return render(request, 'flash_card.html')

def quiz(request):
    return render(request, 'spelling.html')

def multiplechoice(request):
    return render(request, 'mcq.html')

def calendar(request):
    return render(request, 'calendar.html')

#speaking topics
def speaking_topics(request):
    return render(request, 'speaking_topics.html')