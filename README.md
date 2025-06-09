# streamlit-react

Build Streamlit apps with React-like syntax in Python. This library provides a seamless way to create interactive web applications using familiar React patterns while staying in the Python ecosystem.

## Features

- **React-like syntax** - Write UI components using familiar React patterns
- **Context management** - Built-in state management and component context
- **Event handling** - Interactive components with onChange callbacks  
- **TypeScript frontend** - Modern React + TypeScript + Vite frontend
- **Tailwind CSS** - Utility-first CSS framework for styling

## Quick Start

```python
import streamlit as st
import streamlit_react as sr

# Create interactive components
def counter_app():
    if 'count' not in st.session_state:
        st.session_state.count = 0
    
    def increment():
        st.session_state.count += 1
    
    with sr.element("div", className="p-4 bg-white rounded-lg shadow"):
        sr.element("h1", "Counter App", className="text-2xl font-bold mb-4")
        sr.element("p", f"Count: {st.session_state.count}", className="text-lg mb-4")
        sr.element("button", "Increment", 
                  on_change=increment,
                  className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600")

counter_app()
```

## Installation

```bash
pip install streamlit-react
```

## Development

### Setup
```bash
# Install Python dependencies
pip install -e .

# Install frontend dependencies
cd frontend
yarn install
```

### Build
```bash
# Build frontend
./scripts/build_frontend.sh

# Run development server
./scripts/dev.sh
```

## API Reference

### `element(name, *children, **props)`
Create a UI element with optional children and properties.

### `text(value, **props)`
Create a text element with the specified value.

### Context Management
- Elements automatically inherit parent context
- State management through Streamlit session state
- Event handling with `on_change` callbacks

## License

MIT License - see [LICENSE](LICENSE) for details.