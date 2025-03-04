# Sample Python code for youtube.liveBroadcasts.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
import pprint

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import threading



class YouTube():
    def __init__(self):
        self.youtube = None

    def start_poll(self): # use lock
        threading.Timer(5.0, self.poll_chat).start()

    def poll_chat(self):
        print("polling chat")
        request = self.youtube.liveBroadcasts().list(
            part="snippet,contentDetails,status",
            broadcastType="all",
            mine=True
        )
        response = request.execute()
  
        print('GETTING CHATS')

        if "liveChatId" in response["items"][0]["snippet"]:
            request = self.youtube.liveChatMessages().list(
                liveChatId=response["items"][0]["snippet"]["liveChatId"],
                part="snippet"
            )
        response = request.execute()
        pprint.pprint(response)
        self.start_poll()

    def get_live_broadcast(self):
        # -*- coding: utf-8 -*-
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "./chatrooms/youtube/client_secret.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        
        credentials = flow.run_console()
        self.youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        request = self.youtube.liveBroadcasts().list(
            part="snippet,contentDetails,status",
            broadcastType="all",
            mine=True
        )
        response = request.execute()
  
        print('GETTING CHATS')

        if "liveChatId" in response["items"][0]["snippet"]:
            request = self.youtube.liveChatMessages().list(
                liveChatId=response["items"][0]["snippet"]["liveChatId"],
                part="snippet"
            )
        response = request.execute()
        print(response)
        self.start_poll()
