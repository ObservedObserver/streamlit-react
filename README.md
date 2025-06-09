# Streamlit React

Build Streamlit apps with React-like syntax in Python. Write web apps using familiar React patterns while staying in the Python ecosystem.

## Features

- **React-like syntax**: Use familiar React patterns and JSX-style element creation
- **Python native**: No JavaScript required - everything in Python
- **Streamlit integration**: Seamless integration with Streamlit's ecosystem
- **TypeScript frontend**: Built with modern React, TypeScript, and Vite
- **State management**: Built-in state handling with Streamlit's session state
- **Event handling**: Support for interactive elements with event callbacks

## Quick Start

### Installation

```bash
pip install streamlit-react
```

### Basic Usage

```python
import streamlit as st
import streamlit_react as sr

# Create elements with React-like syntax
with sr.element("div", className="bg-white p-4 rounded-lg shadow"):
    sr.element("h1", "Hello World", className="text-2xl font-bold")
    sr.element("p", "This is a paragraph", className="text-blue-500")
    
    # Interactive elements with callbacks
    def handle_click():
        st.session_state.counter += 1
    
    sr.element("button", "Click me!", 
               onClick=handle_click,
               className="bg-blue-500 text-white px-4 py-2 rounded")
```

## Development

### Prerequisites

- Python 3.8+
- Node.js 16+
- Yarn

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/streamlit-react.git
cd streamlit-react
```

2. Install Python dependencies:
```bash
pip install -e .
```

3. Install frontend dependencies:
```bash
cd frontend
yarn install
```

4. Build the frontend:
```bash
yarn build
```

### Running Examples

```bash
streamlit run Home.py
```

### Development Scripts

- `scripts/dev.sh` - Start development environment
- `scripts/frontend.sh` - Start frontend development server
- `scripts/build.sh` - Build the project
- `scripts/build_frontend.sh` - Build frontend only

## API Reference

### Element Creation

```python
sr.element(tag, children=None, **props)
```

- `tag`: HTML tag name (div, span, button, etc.)
- `children`: Text content or nested elements
- `**props`: HTML attributes and event handlers

### Text Elements

```python
sr.text(content)
```

Simple text rendering without HTML wrapper.

## Examples

### Counter App

```python
import streamlit as st
import streamlit_react as sr

if 'counter' not in st.session_state:
    st.session_state.counter = 0

def increment():
    st.session_state.counter += 1

with sr.element("div", className="text-center p-8"):
    sr.element("h1", f"Count: {st.session_state.counter}", 
               className="text-4xl font-bold mb-4")
    sr.element("button", "Increment", 
               onClick=increment,
               className="bg-blue-500 text-white px-6 py-2 rounded hover:bg-blue-600")
```

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

Built on top of the excellent [Streamlit](https://streamlit.io/) framework and [streamlit-component-lib](https://github.com/streamlit/streamlit).