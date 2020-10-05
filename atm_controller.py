#!/usr/bin/python3


"""
INSTRUCTIONS:
 Write code for a simple ATM

At least the following flow should be implemented:

Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw

For simplification, there are only 1 dollar bills in this world, no cents. Thus account balance can be represented in integer.
Your code doesn't need to integrate with a real bank system, but keep in mind that we may want to integrate it with a real bank system
 in the future. It doesn't have to integrate with a real cash bin in the ATM, but keep in mind that we'd want to integrate with that
  in the future. And even if we integrate it with them, we'd like to test our code. Implementing bank integration and ATM hardware
  like cash bin and card reader is not a scope of this task, but testing the controller part (not including bank system, cash bin etc)
   is within the scope.
A bank API wouldn't give the ATM the PIN number, but it can tell you if the PIN number is correct or not.

Based on your work, another engineer should be able to implement the user interface. You don't need to implement any
    REST API, RPC, network communication etc, but just functions/classes/methods, etc.

You can simplify some complex real world problems if you think it's not worth illustrating in the project.
"""


class ATMController:
    def __init__(self, atm_serial_number):
        self.overdraft = 300.00  # default value for overdraft
        self.balance = 0.00  # TODO: fetch balance based on user info after populating

        self.atm_cash_bin = 100000  # TODO: set this cash amount depending on the atm that is being used (based on atm serial number)

    def _raise_warning_message(self, msg):
        # TODO: output message to console for user to modify their action
        print(msg)

    def prompt_to_insert_card(self):  # can also rename to insert_card
        # wait for card to be present
        # include interrupt for cancelling
        pass

    def get_system_info(self):  # TODO: should populate some goodies
        pass

    def read_card(self):
        pass

    def prompt_to_enter_pin(self):  # can also rename to enter_pin
        # wait for pin to be entered
        pass

    def select_account(self):
        pass

    def display_balance(self):
        pass

    def deposit(self, amount):
        if amount >= 0:
            # raise message
            self._raise_warning_message("Please deposit an amount that is greater than 0")
        pass

    def withdraw(self, amount):
        if amount > (self.overdraft + self.balance):
            self._raise_warning_message("Insufficient funds. Your current balance is {}".format(self.balance))
            return False
        self.balance -= amount
        self.output_money(amount)
        self._raise_warning_message("New balance is {}".format(self.balance))  # TODO: can add some message if account is in overdraft
        return True

    def output_money(self, amount):
        # outputs money from ATM to user
        pass

    def other_stuff(self):
        pass
