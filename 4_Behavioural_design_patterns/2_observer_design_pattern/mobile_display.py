from observer import Observer
class MobileDisplay(Observer):
    def update_temp(self, new_temp):
        print(f"Mobile temperature updated to: {new_temp}")