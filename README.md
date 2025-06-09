# streamlit-react

Build Streamlit apps with React-like syntax in Python. Write declarative UI components using familiar React patterns while staying in Python.

## Features

- **React-like syntax** - Use JSX-style components in Python
- **Event handling** - Interactive components with state management
- **Tailwind CSS** - Built-in styling support
- **TypeScript frontend** - Type-safe React components under the hood
- **Streamlit integration** - Seamless integration with Streamlit apps

## Quick Start

```python
import streamlit as st
import streamlit_react as sr

# Create interactive elements with React-like syntax
with sr.element("div", className="p-4 bg-white rounded-lg shadow"):
    sr.element("h1", "Hello World", className="text-2xl font-bold")
    sr.element("p", "Interactive Streamlit with React", className="text-gray-600")
    
    # Add interactive input with event handling
    sr.element("input", 
               on_change=handle_input,
               className="mt-4 px-3 py-2 border rounded")
```

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd streamlit-react

# Install Python dependencies
pip install streamlit

# Install frontend dependencies
cd frontend
yarn install
cd ..

# Run the development server
streamlit run Home.py
```

## Development

```bash
# Start frontend development server
./scripts/frontend.sh

# Build frontend for production
./scripts/build_frontend.sh

# Run full development environment
./scripts/dev.sh
```

## Project Structure

```
streamlit-react/
├── streamlit_react/          # Python package
│   ├── base/                 # Core components
│   └── utils/               # Utilities
├── frontend/                # React/TypeScript frontend
│   └── src/                 # React components
├── scripts/                 # Build and development scripts
└── Home.py                  # Example Streamlit app
```

## License

MIT License