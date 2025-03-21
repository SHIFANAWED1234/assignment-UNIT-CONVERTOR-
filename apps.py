import streamlit as st

# Apply custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg,#bcbcbc,#cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: #333333;
    }
    .stButton>button {
        background: linear-gradient(135deg,#bcbcbc,#cfe2f3);
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        transition: background 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg,#bcbcbc,#a2d2ff);
        color: black;
    }
    .result-box {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        background: rgba(135, 194, 243, 0.2);
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 5px 8px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: #666666;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1>Google Unit Converter</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# Select conversion type
conversion_types = st.sidebar.selectbox("Choose conversion type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert", value=1.0)

# Define columns for unit selection
col1, col2 = st.columns(2)

# Function to get units based on conversion type
def get_units(conversion_type):
    if conversion_type == "Length":
        return ["Meter", "Kilometer", "Mile", "Yard", "Feet", "Inches"]
    elif conversion_type == "Weight":
        return ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
    elif conversion_type == "Temperature":
        return ["Celsius", "Fahrenheit", "Kelvin"]
    return []

units = get_units(conversion_types)

with col1:
    from_unit = st.selectbox("From unit", units)
with col2:
    to_unit = st.selectbox("To unit", units)

# Conversion functions
def length_conversion(value, from_unit, to_unit):
    length_units = {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Feet": 0.3048,
        "Inches": 0.0254
    }
    return value * length_units[from_unit] / length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value + 459.67) * 5/9
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value * 9/5) - 459.67
    return value  # If from_unit == to_unit, return the same value

# Perform conversion
if st.button("Convert"):
    try:
        if conversion_types == "Length":
            result = length_conversion(value, from_unit, to_unit)
        elif conversion_types == "Weight":
            result = weight_conversion(value, from_unit, to_unit)
        elif conversion_types == "Temperature":
            result = temperature_conversion(value, from_unit, to_unit)

        st.markdown(f"<div class='result-box'>Result: {result:.4f} {to_unit}</div>", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown("<div class='footer'>Developed by Shifa Nawed </div>", unsafe_allow_html=True)