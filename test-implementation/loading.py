#loads the data from google sheets and converts it into a python-usable manner

import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://googleapis.com/auth/spreadsheets"]

def load_sheet(SPREADSHEET_ID, SHEET_RANGE):
    credentials = None
    if os.path.exists("token.json"):
        print("Credentials: ", credentials)
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not credentials or not credentials.valid: # repair credentials
        if credentials and credentials.expired:
            print("Credentials expired!")

            if credentials.refresh_token:
                credentials.refresh(Request())
                print("Credentials refreshed.")
            else:
                print("Failed to refresh credentials!")
                return

        else: # what???
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            credentials = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(credentials.to_json()) # save repaired credentials

    #print("Loading data from google sheets...")
    #print(f"\tSpreadsheet ID: {SPREADSHEET_ID}\n\tService: {"sheets"} {"v4"}\n\tRange: {"SHEET_RANGE"}")
    try:
        service = build("sheets", "v4", credentials = credentials)
        sheet = service.spreadsheet()# create loader class

        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SHEET_RANGE).execute()
        values = result.get("values",[])

        for row in values:
            print(row)

    except HttpError as error:
        print(error)
