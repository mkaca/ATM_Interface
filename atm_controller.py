#!/usr/bin/python3


"""

Author: Michael Kaca
Date: Oct 6, 2020



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

import time


class ATMController:
    def __init__(self, atm_serial_number):
        self.overdraft = 300.00  # default value for overdraft
        self.pin_retries = 3

        self.atm_cash_bin = None
        self.card_id = None
        self.temp_pin = None
        self.selected_account = None
        self.balance = None

        self.populate_atm_params(atm_serial_number)
        self.flow()  # calls flow during object instantiation for the purpose of this activity

    def _raise_message(self, msg):
        # TODO: output message to console for user to modify their action
        print(msg)

    def populate_atm_params(self, atm_serial_number):
        # TODO: Should populate atm parameters here from server such as setting atm_cash_bin amount + UI parameters
        self.atm_cash_bin = 100000 # placeholder

    def prompt_to_insert_card(self):  # can also rename to insert_card
        # wait for card to be present
        # TODO: include UI interrupt for cancelling
        self._raise_message("Please insert your debit/credit card")
        # wait until card has been detected
        card_detected = False
        timer_start = time.time()  # simple timeout
        timeout = 10
        while not card_detected:  # poll for card detection
            if True:  # placeholder --> in reality, replace True with ATM hardware readings
                card_detected = True
            if time.time() - timer_start > timeout:
                self._raise_message("Failed to detect card within {} seconds".format(timeout))
                return False
        return True

    def populate_user_info(self):  # TODO: should populate some information regarding user + accounts once pin is verified from card
        pass

    def read_card(self):
        # ATM hardware reads card via scanner + verifies that the card is valid
        placeholder_card_id = "1234321235321"
        self.card_id = placeholder_card_id

    def prompt_to_enter_pin(self):  # can also rename to enter_pin
        # wait for pin to be entered
        self._raise_message("Please enter your pin")
        # placeholder for getting pin... obviously hardware would take care of getting the
        #   real pin and temporarily storing it in the ATM
        self.temp_pin = input()  # placeholder

    def select_account(self):
        self._raise_message("Please select an account")
        selected = input()  # would use UI normally
        account = self.set_account(selected)  # fetch object based on selection... TODO: set_account is not implemented since it is out of this project scope
        self.selected_account = account  # where account is actually a custom object that contains balance

    def display_balance(self):
        # assumes balance is in dollars
        self._raise_message("Your current balance is {} dollars".format(self.balance))

    def deposit(self, amount):
        if amount <= 0:  # edge case  --> can also be prompted upon time-out
            # raise message
            self._raise_message("Please deposit an amount that is greater than 0")
        # HW processes money here
        self.balance += amount
        self.atm_cash_bin += amount  # update atm cash bin balance
        self._raise_message("New balance is {}".format(self.balance))

    def withdraw(self, amount):
        if amount > (self.overdraft + self.balance):
            self._raise_message("Insufficient funds. Your current balance is {}".format(self.balance))
            return False
        if self.output_money(amount):
            self.balance -= amount
            self._raise_message("New balance is {}".format(self.balance))  # TODO: can add some message if account is in overdraft
            return True
        return False

    def output_money(self, amount):
        # outputs money from ATM to user
        # if insufficient money inside of ATM, return False
        if self.atm_cash_bin >= amount:
            self.atm_cash_bin -= amount  # update atm cash bin balance
        # TODO: function for HW to return bills based on amount selected... combination of 1,5,10,20,50,100 dollar bills for example
        return True

    def verify_pin(self):
        """
        Verifies that the pin that the user entered matches the pin of the debit/credit card
        :return: boolean ... true if matches
        """
        # fetch pin based on card number
        accepted = self.server_fetch(self.temp_pin)  # TODO fetch is obviously not implemented since \
        #  there is no server involved.... normally would return True if pin matched that in system, false otherwise
        self.temp_pin = None  # reset temp pin for user privacy
        return accepted

    def server_fetch(self, pin):
        return True

    def set_account(self, selected):
        # determines balance based on account
        # self.balance = account.balance  # account object not implemented (out of scope of project)
        # for demo purposes set arbitrary account balance
        self.balance = 2020.00
        return "checking"  # TODO: would return an actual account object

    def flow(self):  # simple atm flow for user interacting with ATM
        # TODO Flow should be better controlled using UI
        if self.prompt_to_insert_card():
            self.read_card()
            for attempt in range(self.pin_retries):  # allows user to retry pin X times
                self.prompt_to_enter_pin()
                if self.verify_pin():
                    break
                elif attempt == (self.pin_retries - 1):
                    self._raise_message("Too many failed attempts!")
                    # TODO: alert security or whatever the desired action here is
                    exit()
            self.populate_user_info()
            self.select_account()
            # allows user to perform any action multiple times while still logged on
            while True:
                # TODO: Can implement timeout
                ui_input = input("Select action")  # this would be done over the UI as well...
                ui_param = 60  # this would be set over the UI
                if ui_input == "withdraw":
                    self.withdraw(ui_param)
                elif ui_input == "deposit":
                    self.deposit(ui_param)
                elif ui_input == "view_balance":
                    self.display_balance()
                elif ui_input == "change_account":
                    self.select_account()
                elif ui_input == "end_session":
                    # End session and exit
                    self._raise_message("Thank you for using Bear Robotics ATM")
                    exit()
                elif ui_input == "whatever_else_needs_to_be_implemented":  # TODO: add whatever methods are needed here
                    pass
                else:
                    raise SystemError("UI input mismatch. ATM needs maintenance.")
        return False


if __name__ == "__main__":
    atm = ATMController("342342")

