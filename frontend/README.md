# Frontend - Streamlit React Components

React/TypeScript frontend for streamlit-react component rendering.

## Tech Stack

- **React 18** - Modern React with hooks
- **TypeScript** - Type-safe development
- **Vite** - Fast build tool and dev server
- **Tailwind CSS** - Utility-first CSS framework
- **Streamlit Component Lib** - Bridge to Streamlit

## Development

```bash
# Install dependencies
yarn install

# Start development server
yarn dev

# Build for production
yarn build

# Lint code
yarn lint

# Preview production build
yarn preview
```

## Project Structure

```
src/
├── element/              # Core element components
│   ├── index.tsx        # Main element component
│   └── registerComponents.ts
├── hooks/               # React hooks
│   └── useAutoHeight.ts
├── App.tsx             # Main app component
└── main.tsx           # Entry point
```

## Configuration

- **Prettier**: Single quotes, 4-space tabs, 160 char width
- **ESLint**: React hooks and refresh rules enabled
- **TypeScript**: Strict mode with modern target
- **Tailwind**: Custom configuration with auto-height utilities