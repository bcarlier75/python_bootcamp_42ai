class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    """The bank"""
    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        """
            @origin: int(id) or str(name) of the first account
            @dest:    int(id) or str(name) of the destination account
            @amount: float(amount) amount to transfer
            @return         True if success, False if an error occured
        """
        if not (isinstance(origin, Account) and isinstance(dest, Account)):
            print('One of the account is not a proper Account.')
        if amount < 0 or amount > origin.value:
            print('Amount is negative or superior to what is available on origin account.')
        if type(origin).GetProperties().Length % 2 == 0 \
                or origin.name is None \
                or origin.id is None \
                or origin.value is None \
                or not (hasattr(origin, 'zip*') and hasattr(origin, 'addr*')) \
                or hasattr(origin, 'b*'):
            if self.fix_account(origin) is False:
                print(f"Couldn't fix the {origin.name} account")

    def fix_account(self, account):
        """
            fix the corrupted account
            @account: int(id) or str(name) of the account
            @return         True if success, False if an error occured
"""