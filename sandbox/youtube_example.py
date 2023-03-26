# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os
import json
from decouple import config

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = config('YOUTUBE_CLIENT_SECRET_FILE')
    print(client_secrets_file)

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # API Requests

    # channel information and statistics
    # request = youtube.channels().list(
    #     part="snippet,contentDetails,statistics",
    #     mine=True
    #     # id="UC_x5XG1OV2P6uZZ5FSM9Ttw"
    # )
    # response = request.execute()
    # print(response)

    # most popular videos
    # request = youtube.videos().list(
    #     part="snippet,statistics",
    #     chart="mostPopular",
    #     regionCode="BR",
    #     maxResults=10,
    #     fields='items(id,snippet(title,channelId,publishedAt),statistics)',
    #     prettyPrint=True
    # )
    # response = request.execute() 
    # print()
    # print(json.dumps(response, indent=2))

    # serch by topic within date and order results
    # q="chat gpt",
    request = youtube.search().list(
        type="video",
        channelType="any",
        regionCode="BR",
        order="viewCount",
        maxResults=10,
        publishedAfter="2023-03-01T00:00:00Z",
        publishedBefore="2023-03-15T00:00:00Z",
        part="snippet",
        fields='items(id,snippet(title,channelTitle,channelId,publishedAt))',
        )
    response = request.execute() 
    print()
    print(json.dumps(response, indent=2))

    # eoc
    print()

if __name__ == "__main__":
    main()