class InvalidOutletException(Exception):
    def __init__(self, id):
        super().__init__("Input outlet {id}".format(id=id))
