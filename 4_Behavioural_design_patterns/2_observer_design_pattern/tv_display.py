from observer import Observer
class TVDisplay(Observer):
    def update_temp(self, new_temp):
        print(f"TV temperature updated to: {new_temp}")