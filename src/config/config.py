import streamlit as st
import os


def set_page(goto_tab, actual_tab):
    f = open('./src/config/page.txt', 'w')
    f.write(f'{goto_tab}')
    f.close()

    if goto_tab != actual_tab:
        st.rerun()



def get_page():
    if not os.path.exists('./src/config/page.txt'):
        f = open('./src/config/page.txt', 'w')
        f.write('0')
        f.close()
        
    f = open('./src/config/page.txt', 'r')
    page = int(f.read(1))
    f.close()
    return page
