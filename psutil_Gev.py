
import psutil


class MyProcess:
    def __init__(self, name):
        self.name = name

    def get_pid(self, name):
        self.name = name
        for process in psutil.process_iter():
            if process.name() == name:
                return process.pid

    def kill_process_by_id(self, name):
        self.name = name
        for process in psutil.process_iter():
            if process.name() == name:
                process.kill()

    def check_proc_run(self, name):
        pid = self.get_pid(name)
        self.name = name
        for process in psutil.process_iter():
            if process.status() == "running" and process.pid == pid:
                return True
        return False

    def start_proc_by_name(self, name):
        self.name = name
        os.system("start %s" + name)


name1 = "notepad.exe"
p = MyProcess(name1)
print(p.get_pid(name1))
print(p.kill_process_by_id(name1))
print(p.check_proc_run(name1))
