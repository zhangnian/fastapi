from blinker import signal

from fastapi.signals.signal_handler import *


sig_user = signal('userinfo_modifiy')



def register_signal_handlers():
    sig_user.connect(on_userinfo_modify)