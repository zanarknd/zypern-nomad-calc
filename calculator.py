import argparse
from dataclasses import dataclass
from decimal import Decimal
from typing import Optional, Union

TWO_PLACES = Decimal(10) ** -2

LEGAL_WARNING = """
Please note that the author of this software is NOT any of the following: 
financial expert, financial advisor, tax expert, tax advisor, accountant.

The author of this software takes no responsibility whatsoever for any way 
in which you chose to utilize this software or its output, and bears no 
liability for the consequences of your usage of the software or its output.

Peruse on your own risk. Consult a professional accountant for tax advise.
"""


@dataclass
class Bracket:
    low: int
    high: Optional[int]
    tax_rate: Decimal

    def calculate_tax(self, gross_base: Decimal) -> Decimal:
        if gross_base > self.low:
            if self.high and gross_base > self.high:
                tax_base = self.high - self.low
            else:
                tax_base = gross_base - self.low

            return (tax_base * self.tax_rate).quantize(TWO_PLACES)

        return Decimal(0)


INCOME_TAX_BRACKETS = [
    Bracket(low=0, high=19500, tax_rate=Decimal(0)),
    Bracket(low=19500, high=28000, tax_rate=Decimal("0.2")),
    Bracket(low=28000, high=36300, tax_rate=Decimal("0.25")),
    Bracket(low=36300, high=60000, tax_rate=Decimal("0.3")),
    Bracket(low=60000, high=None, tax_rate=Decimal("0.35")),
]

GESY_RATE = Decimal("0.0265")


def calculate_income_tax(
    total_gross_to_date: Union[int, float, Decimal],
    current_month_gross: Optional[Union[int, float, Decimal]] = None,
) -> (Decimal, Decimal):

    if not isinstance(total_gross_to_date, Decimal):
        total_gross_to_date = Decimal(total_gross_to_date)
    if current_month_gross and not isinstance(current_month_gross, Decimal):
        current_month_gross = Decimal(current_month_gross)

    current_month_gross = current_month_gross or 0

    total_payable_this_year = sum(
        bracket.calculate_tax(total_gross_to_date) for bracket in INCOME_TAX_BRACKETS
    )

    payable_for_this_salary = total_payable_this_year - (
        sum(
            bracket.calculate_tax(total_gross_to_date - current_month_gross)
            for bracket in INCOME_TAX_BRACKETS
        )
    )

    return total_payable_this_year, payable_for_this_salary


parser = argparse.ArgumentParser(
    description=(
        "A little script that helps you approximate personal income tax per "
        "Cyprus tax laws of 2022. " + LEGAL_WARNING
    )
)

parser.add_argument(
    "total",
    type=float,
    help="Total gross income for the year to date",
)

parser.add_argument(
    "--salary",
    type=float,
    help="Last month's salary (should be included into total)",
)


if __name__ == "__main__":
    args = parser.parse_args()

    print(LEGAL_WARNING)

    total_for_year, tax_for_last_salary = calculate_income_tax(args.total, args.salary)

    print("=== Personal income tax ===")
    print(f"In total this year you owe the state €{total_for_year}.")
    if args.salary:
        print(f"Of which, for the last month's income you owe €{tax_for_last_salary}.")

    print("\n=== GESY ===")
    total_gesy = min(Decimal(args.total) * GESY_RATE, 180_000)
    print(f"In total for the year, you owe the state €{total_gesy:.2f}.")
    if args.salary:
        gesy_for_salary = Decimal(args.salary) * GESY_RATE
        print(f"Of which, for the last month's income you owe €{gesy_for_salary:.2f}.")

    print("\n")
