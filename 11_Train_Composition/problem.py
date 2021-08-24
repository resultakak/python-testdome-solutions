class TrainComposition:
    
    def __init__(self):
        pass
    
    def attach_wagon_from_left(self, wagonId):
        """
        :param wagonId: (int) The number of the wagon to attach to the left
        """
        pass
    
    def attach_wagon_from_right(self, wagonId):
        """
        :param wagonId: (int) The number of the wagon to attach to the right
        """
        pass

    def detach_wagon_from_left(self):
        """
        :returns: (int) The number of the wagon detached from left
        """
        pass
    
    def detach_wagon_from_right(self):
        """
        :returns: (int) The number of the wagon detached from right
        """
        pass

if __name__ == "__main__":
    train = TrainComposition()
    train.attach_wagon_from_left(7)
    train.attach_wagon_from_left(13)
    print(train.detach_wagon_from_right()) # should print 7
    print(train.detach_wagon_from_left()) # should print 13
