from lynx.account import Account
from lynx.consensus.vrf import VRF


def test_vrf():
    account = Account()
    rng = VRF.generate_random_number(account.signing_key)


if __name__ == "__main__":
    test_vrf()