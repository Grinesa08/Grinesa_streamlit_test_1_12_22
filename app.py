import streamlit as st

# our input = Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat

# 1
s = st.text_input('Type the text: ')

# 2
def convert_list(s):
    words = s.split()
    return words

if st.button('Return List'):
    st.write(convert_list(s))

# 3 
def convert_lower(list_converted):
    new_list = []
    for i in list_converted:
        new_list.append(i.lower())
    return new_list

if st.button('Lower'):
    st.write(convert_lower(convert_list(s)))

# 4
def count(given_list):
    count = 0
    for i in given_list:
        count += 1
    return count

if st.button('Print Count'):
    st.write(count(convert_list(s)))

















