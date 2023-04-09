import streamlit as st
from forex_python.converter import CurrencyRates

# Create a currency converter object
converter = CurrencyRates()

# Define a function to convert currency
def convert_currency(amount, from_currency, to_currency):
    rate = converter.get_rate(from_currency, to_currency)
    converted_amount = round(amount * rate, 2)
    return converted_amount

# Define the Streamlit app
def app():
    st.title("Currency Converter")

    # Input amount and currencies to convert
    amount = st.number_input("Enter the amount to convert:")
    from_currency = st.selectbox("From currency:", ["USD", "EUR", "GBP"])
    to_currency = st.selectbox("To currency:", ["USD", "EUR", "GBP"])

    # Convert currency and display result
    if st.button("Convert"):
        result = convert_currency(amount, from_currency, to_currency)
        st.success(f"{amount} {from_currency} = {result} {to_currency}")

# Run the app
if __name__ == '__main__':
    app()
