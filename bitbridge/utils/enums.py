from enum import Enum


class RPCGroup(str, Enum):
    BLOCKCHAIN = "blockchain"
    CONTROL = "control"
    NETWORK = "network"
    RAW_TRANSACTIONS = "raw_transactions"
    UTIL = "util"
    WALLET = "wallet"
