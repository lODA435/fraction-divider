import streamlit as st
from fractions import Fraction

st.set_page_config(page_title="Fraction Divider")

st.title("Ділення дробів")

col1, col2 = st.columns(2)

with col1:
    fraction_input = st.text_input("Перше число:", value="2 17/14")

with col2:
    divisor = st.number_input("Друге число:", value=2.0, step=1.0)

def parse_mixed_fraction(s):
    try:
        s = s.strip()
        if ' ' in s:
            parts = s.split()
            return float(int(parts[0]) + Fraction(parts[1]))
        return float(Fraction(s))
    except:
        return None

def format_mixed_fraction(val):
    frac = Fraction(val).limit_denominator()
    num = frac.numerator
    den = frac.denominator
    if num >= den:
        whole = num // den
        remainder = num % den
        if remainder == 0:
            return f"{whole}"
        return f"{whole} {remainder}/{den}"
    return f"{num}/{den}"

if st.button("Обчислити"):
    val = parse_mixed_fraction(fraction_input)
    
    if val is not None and divisor != 0:
        res_value = val / divisor
        result_text = format_mixed_fraction(res_value)
        st.success(f"Результат: {result_text}")
    elif divisor == 0:
        st.error("Ділення на нуль!")
    else:
        st.error("Помилка формату")
