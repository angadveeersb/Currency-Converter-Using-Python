# Currency Converter
This is a simple currency converter app built using Python and Streamlit. It allows you to convert from one currency to another with real-time exchange rates.
<br>
### Introduction 
The currency converter app is built using the Streamlit framework and the forex_python library, which allows the app to retrieve exchange rates between various currencies.
<br>
The app starts by creating a currency converter object using the `CurrencyRates()` class. Then, it defines a function called `convert_currency()` that takes three arguments - the amount to convert, the currency to convert from, and the currency to convert to. This function uses the `get_rate()` method of the currency converter object to retrieve the exchange rate between the two currencies, and then multiplies the amount to convert by this exchange rate to calculate the converted amount.
<br>
If there is an error retrieving the exchange rate (for example, if one of the specified currencies is not supported), the function returns None and displays an error message using the `write()` method of the Streamlit framework.
<br>
The Streamlit app defines a UI with two dropdown menus to select the currencies to convert from and to, and a text input to specify the amount to convert. When the "Convert" button is clicked, the app calls the convert_currency() function with the specified inputs and displays the result using the write() method.
<br>
Finally, the __name__ variable is checked to ensure that the app is being run directly (as opposed to being imported as a module), and if so, the app() function is called to run the Streamlit app.<br>
### Usage
1. Select the "From" currency and the "To" currency from the dropdown menus.<br>
2. Enter the amount of money you want to convert.<br>
3. Click on the "Convert" button.<br>
4. The converted amount will be displayed below.<br>
### Supported Currencies
The following currencies are currently supported by the app:<br>

AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN, BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL, BSD, BTC, BTN, BWP, BYN, BYR, BZD, CAD, CDF, CHF, CLF, CLP, CNH, CNY, COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD, EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS, GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF, IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD, JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT, LAK, LBP, LKR, LRD, LSL, LYD, MAD, MDL, MGA, MKD, MMK, MNT, MOP, MRO, MRU, MUR, MVR, MWK, MXN, MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB, PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB, RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS, SPL, SRD, SSP, STN, SVC, SYP, SZL, THB, TJS, TMT, TND, TOP, TRY, TTD, TVD, TWD, TZS, UAH, UGX, USD, UYU, UZS, VEF, VES, VND, VUV, WST, XAF, XAG, XAU, XCD, XDR, XOF, XPD, XPF, XPT, YER, ZAR, ZMW, ZWL
<br>
### Hosted Link
You can access the hosted app at https://deepankarvarma-currency-converter-using-python-app-5xebdz.streamlit.app/
