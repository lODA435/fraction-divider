import streamlit as st
from fractions import Fraction

# Налаштування сторінки
st.set_page_config(page_title="Fraction Divider", page_icon="🧮")

st.title("🧮 Ділення мішаного дробу")
st.write("Введи дріб у форматі `ціле чисельник/знаменник` (наприклад, `2 17/14`) та число для ділення.")

# Створюємо дві колонки для полів введення
col1, col2 = st.columns(2)

with col1:
    fraction_input = st.text_input("Мішаний дріб:", value="2 17/14")

with col2:
    divisor = st.number_input("Дільник (число):", value=2.0, step=1.0)


def parse_mixed_fraction(s):
    try:
        s = s.strip()
        if ' ' in s:
            # Розділяємо цілу частину та дробову
            whole_part, frac_part = s.split(' ')
            whole = int(whole_part)
            frac = Fraction(frac_part)
            # Для додатних чисел: ціле + дріб
            return float(whole + frac)
        else:
            # Якщо ввели просто дріб або просто число
            return float(Fraction(s))
    except Exception:
        return None


# Обчислення
if st.button("Обчислити"):
    val = parse_mixed_fraction(fraction_input)

    if val is None:
        st.error("Помилка! Перевір формат дробу. Має бути наприклад: `2 17/14` або `1/2`")
    elif divisor == 0:
        st.warning("На нуль ділити не можна!")
    else:
        result = val / divisor

        # Виведення результату
        st.success(f"### Результат: {result:.4f}")

        # Додатково: відображення у вигляді звичайного дробу
        res_fraction = Fraction(val / divisor).limit_denominator()
        st.info(f"У вигляді простого дробу: `{res_fraction}`")

# Додаткова інструкція
with st.expander("Як користуватися?"):
    st.write("""
    1. У перше поле впиши число. Між цілою частиною і дробом має бути **пробіл**.
    2. У друге поле впиши на що ділимо.
    3. Натисни кнопку 'Обчислити'.
    """)