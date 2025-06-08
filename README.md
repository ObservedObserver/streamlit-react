# streamlit-react

Build Streamlit apps with React-like syntax in Python. Write modern, component-based UIs using familiar React patterns while staying in the Python ecosystem.

## Features

- **React-like syntax** - Use context managers and element composition patterns familiar to React developers
- **Component-based architecture** - Build reusable UI components with props and state management
- **Event handling** - Handle user interactions with `on_change` callbacks
- **Streamlit integration** - Seamlessly integrates with existing Streamlit applications
- **TypeScript frontend** - Modern React + TypeScript frontend with Tailwind CSS support

## Quick Start

```python
import streamlit as st
import streamlit_react as sr

# Simple example
with sr.element("div", className="p-4 bg-blue-100 rounded"):
    sr.element("h1", "Hello World", className="text-2xl font-bold")
    sr.element("p", "This is a paragraph", className="text-blue-500")

# Interactive example with state
if 'counter' not in st.session_state:
    st.session_state.counter = 0

def increment():
    st.session_state.counter += 1

sr.element("button", "Click me", 
           on_change=increment,
           className="px-4 py-2 bg-blue-500 text-white rounded")
st.write(f"Counter: {st.session_state.counter}")
```

## Installation

```bash
pip install streamlit-react
```

## Development

```bash
# Install dependencies
cd frontend && yarn install

# Start development server
./scripts/dev.sh

# Build for production
./scripts/build.sh
```

## License

MIT