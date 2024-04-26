#loads the data from google sheets and converts it into a python-usable manner

import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from std import *

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

def load_sheet(SPREADSHEET_ID, SHEET_RANGE):
    credentials = None
    if os.path.exists("token.json"):
        credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
        dprint(f"Token.json credentials: {credentials} \n")

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

    print("Loading data from google sheets...")
    print(f"Spreadsheet ID: {SPREADSHEET_ID}, Service: (sheets, v4), Range: {SHEET_RANGE}")

    try:
        service = build("sheets", "v4", credentials = credentials)
        sheet = service.spreadsheets()# create loader class

        result = (
            sheet.values()
            .get(spreadsheetId=SPREADSHEET_ID, range=SHEET_RANGE)
            .execute()
        )

        values = result.get("values",[])
        print("Sheet loaded :)\n")

        for row in values:
            dprint(row)

        return values

    except HttpError as error:
        print(error)
        return

load_sheet("1Mn5APkaN1wZov8NB-fzREIPhW9JKVpttO47U-dG319k", "Sheet1!A1:E5")
load_sheet("1Mn5APkaN1wZov8NB-fzREIPhW9JKVpttO47U-dG319k", "Sheet2!A1:B9")