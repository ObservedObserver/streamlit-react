const ComponentCollection = {
} as const;

export function getComponent(componentName: string) {
    if (componentName in ComponentCollection) {
        return ComponentCollection[componentName as keyof typeof ComponentCollection];
    }
    
    // Check if the componentName is a valid HTML element
    if (typeof document.createElement(componentName).tagName === 'string') {
        return componentName;
    }
    
    return false;
}