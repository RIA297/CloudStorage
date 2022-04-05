import dropbox
import os
from dropbox.files import WriteMode
class Transfer_Data:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):

            for filename in files:
                local_path=os,path.join(root,filename)
                relative_path=os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

      
def main():
    access_token="sl.BFJ6kZqsM0Rq4ya-x_KKcqa0bMTYj2IZ8-49Z7I9ZDzCE7WFJkvP0-2AtoWadBVS-I0ZcqRXQSFW_H8sA00VOhDF3IeA_x1Fqqd014pnZgwqgpwJxacwB_gVwvJ7MeaiQOWARYXSV8qY"
    transfer_Data=Transfer_Data(access_token)
    file_from=input("Enter the file path to transfer")
    file_to=input("Enter the full path to upload to dropbox")
    # Api
    transfer_Data.upload_file(file_from,file_to)
    print("File has been moved")
main()
