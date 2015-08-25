from nelsnmp.oids import GeneralOids


class AirespaceOids(GeneralOids):
    """Statically define AirespaceOids (Cisco) OIDs and inherit general oids

    """

    def __init__(self):

        super(AirespaceOids, self).__init__()

        # From AIRESPACE-SWITCHING-MIB
        self.agentInventoryProductVersion = '1.3.6.1.4.1.14179.1.1.1.14'
