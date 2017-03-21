class Event(object):
    """
    Something that happens in the system
    """
    def __init__(self, trigger):
        self.trigger = trigger


class Click(Event):
    pass
