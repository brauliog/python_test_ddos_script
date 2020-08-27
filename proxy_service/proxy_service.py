from torrequest import TorRequest



def tor_connect():
    # makes initial tor connection
    tr = TorRequest(password='your_unhashed_password here')
    return tr


def reset_tor_con(tor):
    #resets the tor service
    tor.reset_identity()
    return tor
