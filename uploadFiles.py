import dropbox
import os
from dropbox.files import WriteMode
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)
        
        for root,dirs,files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root,filename)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = 'sl.BPo6QhnqsM9gYMBcMmcoRn-8_JHuv5eEaJZyHu3IawinyRRKuwweguauFyWZ8WZTbhY6SbJpgY_HiQQNNA3yzTnfJfpAATeQXftpkpbBkij5U4FaQrg5gDQRJoCHD_9_Ilcv12nUi9I'
    transferData = TransferData(access_token)

    file_from = input("Enter the folder name which you want to upload = ")
    file_to = input("Enter the path where you want to upload = ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("Folder uploaded succecfully")

if __name__ == '__main__':
    main()