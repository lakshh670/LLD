class Log():
    __instance=None
    def __new__(cls,file_name:str):
        if cls.__instance==None:
            cls.__instance=super().__new__(cls)
            cls.__filename=file_name
            cls.__log_count=0
            return cls.__instance
        else:
            return cls.__instance
    def log(self,msg:str):
        print(f"Logging {msg} into {self.__filename}")
        self.__log_count+=1
    def get_log_count(self):
        return self.__log_count

log1=Log("app.log")
log2=Log("app.log")
log3=Log("app.log")
log1.log("Hey")
log2.log("Good")
log3.log("Bye")
print(log1.get_log_count())
log4=Log("app.log")
log4.log("Salman Khan")