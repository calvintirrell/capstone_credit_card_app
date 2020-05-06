def get_features(selection):
    # use 'selection' to retrieve inputs to use in model

    if selection == "James_Bond":
        #    [...1] = Approved
        jb = [1, 52, 15, 1, 0, 1, 7, 5.5, 1, 1, 14, 0, 2200]
        return jb

    elif selection == "Hermoine_Granger":
        #    [...1] = Approved
        hg = [0, 30, 0.5, 1, 0, 1, 7, 1.75, 1, 1, 11, 0, 540]
        return hg

    elif selection == "Catwoman":
        #   [...0] = Denied
        c = [0, 37, 2.665, 1, 0, 2, 7, 0.165, 0, 0, 0, 0, 501]
        return c

    else: # Maverick
        #   [...0] = Denied
        m = [1, 57, 2, 1, 0, 5, 2, 6.5, 0, 1, 1, 0, 10]
        return m