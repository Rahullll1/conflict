class parent:
    def show(self):
        print("inside parent")
class child(parent):
    def show(self):
        super().show()
        print('inside child')