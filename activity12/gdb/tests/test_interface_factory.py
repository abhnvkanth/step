# gdb/tests/test_interface_factory.py
from gdb.domain.account_factory import AccountFactory

def main():
    print("=== Activity 12: Factory-Driven System Suite ===")

    # TODO (Step 1): Create one account of each type ONLY through AccountFactory.create_account():
    #   "SAVINGS", "CURRENT", "SALARY" and "FIXEDDEPOSIT"
    #   (arguments: account_type, account_number, name, age, balance, status, pin).
    savings = AccountFactory.create_account(
        "SAVINGS", "SA001", "Alice", 25, 10000.0, "Active", "1234"
    )

    current = AccountFactory.create_account(
        "CURRENT", "CA001", "Bob", 35, 50000.0, "Active", "5678"
    )

    salary = AccountFactory.create_account(
        "SALARY", "SAL001", "Charlie", 30, 30000.0, "Active", "1111"
    )

    fixed_deposit = AccountFactory.create_account(
        "FIXEDDEPOSIT", "FD001", "David", 40, 100000.0, "Active", "9999"
    )

    accounts = [savings, current, salary, fixed_deposit]

    # TODO (Step 2): Using only IAccount members (no concrete class names), assert that each account
    #   balance and get_account_type() match what you created, then exercise deposit()/withdraw().
    expected_balances = [10000.0, 50000.0, 30000.0, 100000.0]
    expected_types = ["Savings", "Current", "Salary", "FixedDeposit"]

    for account, expected_balance, expected_type in zip(
        accounts, expected_balances, expected_types
    ):
        assert account.balance == expected_balance
        assert account.get_account_type() == expected_type

        account.deposit(1000.0)
        assert account.balance == expected_balance + 1000.0

        account.withdraw(500.0)
        assert account.balance == expected_balance + 500.0
if __name__ == "__main__":
    main()
