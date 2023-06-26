class IznimkaPostojeciEmail(Exception):
    def __init__(self):
        super(IznimkaPostojeciEmail, self).__init__('Upisani email se već koristi!')