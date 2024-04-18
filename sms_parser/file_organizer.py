
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def authenticate():
  gauth = GoogleAuth() # Path to your credential file
  gauth.LocalWebserverAuth() # Authenticate and get authorization code
  return GoogleDrive(gauth) 

def list_files_recursive(drive, folder_id, indent=0):
  """Recursively lists files in a Google Drive folder and its subfolders."""
  file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()

  for file in file_list:
    if file['mimeType'] == 'application/vnd.google-apps.folder':  # If it's a folder
      print("-" * indent + file['title'])
      list_files_recursive(drive, file['id'], indent + 2)  # Recurse
    else:
      print("-" * indent + file['title']) 

# Authentication
drive = authenticate()

# Replace 'root' with the actual ID of your Google Drive main folder
list_files_recursive(drive, 'root') 