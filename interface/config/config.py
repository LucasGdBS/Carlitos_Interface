import streamlit as st

def set_page(goto_tab, actual_tab):
    f = open("./config/page.txt", "w")
    f.write(f"{goto_tab}")
    f.close()
    
    if goto_tab != actual_tab:
        st.rerun()


def get_page():
    f = open("./config/page.txt")
    page = int(f.read(1))
    f.close()
    
    return page