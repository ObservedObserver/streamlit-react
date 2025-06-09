# Frontend - streamlit-react

React + TypeScript + Vite frontend for the streamlit-react component library.

## Overview

This frontend renders React components from Python streamlit-react elements. It uses:

- **React 18** with TypeScript for type safety
- **Vite** for fast development and building
- **Tailwind CSS** for utility-first styling
- **streamlit-component-lib** for Streamlit integration

## Development

### Scripts

```bash
# Start development server
yarn dev

# Build for production
yarn build

# Lint code
yarn lint

# Preview production build
yarn preview
```

### Project Structure

```
src/
├── App.tsx              # Main app component
├── element/             # Element rendering system
│   ├── index.tsx        # Element renderer
│   └── registerComponents.ts  # Component registration
├── hooks/
│   └── useAutoHeight.ts # Auto-height hook for Streamlit
└── main.tsx            # App entry point
```

## Component Registration

The `registerComponents.ts` file handles mapping element names to React components. Add new components here to extend the element system.

## Styling

Uses Tailwind CSS with custom configuration. Classes are applied directly from Python using the `className` prop.

## Building

The build process:
1. TypeScript compilation
2. Vite bundling
3. Output to `dist/` directory
4. Integration with Python package