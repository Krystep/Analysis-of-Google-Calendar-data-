# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 10:28:30 2022

@author: Kry

accessing Google Calendar 
"""

from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

#creating a scope of acces to Google Api Calendar
scopes = ['https://www.googleapis.com/auth/calendar.readonly']

#authorization process
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
credentials = flow.run_console()

#saving the authorization code to pickle
pickle.dump(credentials, open("token.pkl", "wb")) 
credentials = pickle.load(open("token.pkl", "rb"))

service = build("calendar", "v3", credentials=credentials)

#creating calendar list
result = service.calendarList().list().execute()

#choosing the appropriate calendar
calendar_id = result['items'][0]['id']

#result = service.events().list(calendarId=calendar_id).execute()
#print(result['items'][0])