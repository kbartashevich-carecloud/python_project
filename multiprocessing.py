from multiprocessing import Process

class PrintProcess(Process):
    def __init__(self, name):
        super().__init_()
        self.name = name

    def run(self):
        print("hello", self.name)

p = PrintProcess("Mike")
p.start()
p.join()

