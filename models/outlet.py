from exceptions.invalid_outlet_exception import InvalidOutletException
import threading


'''
This class is the class for the tap of the coffee machine.

- An outlet might be out of order [controlled by is_functioning]
- An outlet might be dispensing [defined by in_use]
- An outlet has an id to uniquely identify it
'''
class Outlet():
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get("id")
        self.is_functioning = True
        self.in_use = False
        self.lock = threading.Lock()

    def is_functional(self):
        if not self.is_functioning:
            raise InvalidOutletException(self.id)
        return True

    ## Added lock to make edits thread safe
    def start(self):
        with self.lock:
            if not self.status():
                raise InvalidOutletException(self.id)
            self.in_use = True

    def stop(self):
        self.in_use = False

    def status(self):
        return self.is_functional() and not self.in_use

    def __str__(self):
        return "'id': '{id}', 'is_functioning':'{is_functioning}', 'in_use': '{in_use}'".format(
            id=self.id,
            is_functioning=self.is_functioning,
            in_use=self.in_use
        )

    def __repr__(self):
        return "'id': '{id}', 'is_functioning':'{is_functioning}', 'in_use': '{in_use}'".format(
            id=self.id,
            is_functioning=self.is_functioning,
            in_use=self.in_use
        )
