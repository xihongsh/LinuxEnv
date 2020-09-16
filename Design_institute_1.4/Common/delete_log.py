import os
class DeleteLogFile:
    def __init__(self,path_1,path_2):
        self.path_1 = path_1
        self.path_2 = path_2
    def delete_file(self):
        for path in [self.path_1,self.path_2]:
            all_log_files = os.listdir(path)
            all_log_files.sort()
            for num in range(len(all_log_files)):
                os.remove(os.path.join(path,all_log_files[num]))




