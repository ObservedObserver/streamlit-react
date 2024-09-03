import streamlit as st
import streamlit_react as sr

# st.title("Home")

# with sr.element("div", className="rounded-lg p-4 shadow-lg bg-white border"):
#     sr.element("h1", "Hello World", className="text-2xl font-bold")
#     sr.element("p", "This is a paragraph", className="text-blue-500")

import streamlit_react as sr

# from streamlit_react import ChevronRightIcon
st.set_page_config(layout="wide")

import streamlit_react as sr

if 'count' not in st.session_state:
    st.session_state.counter = 0

def counter_add():
    st.session_state.counter += 1
    print("Counter Value: ", st.session_state.counter)

def render_hero_section():
    print(st.session_state.counter)
    with sr.element("div", className="bg-gradient-to-t from-zinc-50 to-white dark:from-zinc-950 to-black relative"):
        sr.element("div", className="absolute bg-[url('https://ui.convertfa.st/_convertfast/gradient-bg-0.svg')] bg-auto bg-no-repeat z-0 inset-0 top-0 bottom-0 left-0 right-0 grayscale")
        
        with sr.element("div", className="max-w-7xl mx-auto px-4 py-32 relative z-10"):
            with sr.element("div", className="max-w-3xl"):
                sr.element("h1", "Build Streamlit apps with React in Python", 
                           className="text-6xl font-bold tracking-tight text-primary mb-6 drop-shadow-md")
                
                sr.element("p", "Build web apps with Python. Coding like using React, but in Python.", 
                           className="text-2xl text-gray-600 dark:text-gray-300 mb-8")
                
                with sr.element("div", className="flex gap-4"):
                    with sr.element("a", href="#start", 
                                    className="rounded-md bg-rose-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-rose-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-rose-600"):
                        sr.text("Start now")
                    
                    with sr.element("button", 
                                    className="rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50"):
                        sr.text("npm install convertfast-ui")
                
                sr.element("p", "Open Source. MIT License.", 
                           className="mt-4 text-sm text-gray-500")
                sr.element("input", on_change=counter_add, className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 text-sm leading-6")
            
            # sr.element("img", 
            #            alt="app screenshot",
            #            src="https://ui.convertfa.st/images/graphic-walker-light-2.png",
            #            width="2432",
            #            height="1442",
            #            className="mt-8 rounded-md shadow-2xl border mt-12 block dark:hidden")
            
            # sr.element("img", 
            #            alt="app screenshot",
            #            src="https://ui.convertfa.st/images/graphic-walker-dark-2.png",
            #            width="2432",
            #            height="1442",
            #            className="mt-8 rounded-md shadow-2xl border mt-12 hidden dark:block")

# Call the function to render the hero section
render_hero_section()

st.write("Counter Value: ", st.session_state.counter)

# print(st.session_state.get('_st_react_state'))