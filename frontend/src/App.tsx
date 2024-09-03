import { useRef, useState } from 'react';
import { ComponentProps, withStreamlitConnection } from 'streamlit-component-lib';

import { useAutoHeight } from './hooks/useAutoHeight';
import { ElementRenderer } from './element/index';

type ElementProps = { comp: string; props: any; [key: string]: any };

const App = withStreamlitConnection(function App(cprops: ComponentProps) {
    const { args, width, disabled, theme } = cprops;
    const { comp, props } = args as ElementProps;
    const container = useRef(null);
    const safeHeight = args.safeHeight ?? 10;
    if (import.meta.env.DEV) {
        console.log('DEV MODE', args.comp);
    }
    // TODO: different safe-height for different components
    // 10px is the minimum safe height for slider, while most of the other components do not need it.
    useAutoHeight(container, safeHeight);
    console.log('app', props);
    return <div>
        <ElementRenderer tree={props.tree} ref={container} />
    </div>;
});

export default App;
