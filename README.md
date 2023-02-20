# Cyprus Digital Nomad income tax approximation script

## LEGAL DISCLAIMER

Please note that the author of this software is NOT any of the following: 
financial expert, financial advisor, tax expert, tax advisor, accountant.

The author of this software takes no responsibility whatsoever for any way 
in which you chose to utilize this software or its output, and bears no 
liability for the consequences of your usage of the software or its output.

Peruse on your own risk. Consult a professional accountant for tax advise.

## Description

This is a simple script designed to approximate the amount of personal income tax and GESY contributions one would be obliged to pay if they were a tax resident of the Republic of Cyprus in the year 2022, working remotely for an overseas employer (and thus not entitled to any sorts of tax discounts, benefits or other contributions).

The tax rates and other numbers used in the calculation are observed from publically available sources such as https://www.pwc.com.cy/en/publications/assets/tff-eng-2022.pdf.

Sample usage and output, assuming you earn a salary of €2150 for 12 months without change:
```
$ python calculator.py 25800 --salary 2150

Please note that the author of this software is NOT any of the following:
financial expert, financial advisor, tax expert, tax advisor, accountant.

The author of this software takes no responsibility whatsoever for any way
in which you chose to utilize this software or its output, and bears no
liability for the consequences of your usage of the software or its output.

Peruse on your own risk. Consult a professional accountant for tax advise.

=== Personal income tax ===
In total this year you owe the state €1260.00.
Of which, for the last month's income you owe €430.00.

=== GESY ===
In total for the year, you owe the state €683.70.
Of which, for the last month's income you owe €56.98.

```
