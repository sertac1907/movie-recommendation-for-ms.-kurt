import streamlit as st
import random
import time

st.set_page_config("wide")

word_list = ["aşkım","bebeğim","meleğim","çiçeğim","böceğim","sevgilim","birtanem","hayatım","kadınım","hayatımın anlamı","balım","fıstığım","beyaz peynirim"]
cok_list = ["ÇOK"]

col1, col2 = st.columns(2)


with col2:
    pass


with col1:
    with st.empty():
        while True:
            cok = random.choice(cok_list)
            complement = random.choice(word_list)
            st.write(f"""         ┌───── •✧✧• ─────┐

            SENİ {cok} SEVİYORUM {complement.upper()}
            
            └───── •✧✧• ─────┘""")
            time.sleep(0.45)