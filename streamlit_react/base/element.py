from typing import List, Optional, Any, Dict, Union, Callable
from streamlit_react.base.session import init_element_state
from streamlit_react.utils.declare import declare_component
from .context import get_context
import streamlit as st

component_func = declare_component("element")

def init_default_state(key: str = None, default_value: Any = None, **component_state):
    return {
        "st_key": key,
        "value": default_value,
        "event_id": f"{key}_init",
        **component_state,
    }

class UIElement:
    def __init__(
        self,
        name: str,
        props: Optional[Dict[str, Any]] = None,
        key: Optional[str] = None,
        default_value: Any = None,
        default_component_state: Any = {},
        on_change: Optional[Callable[[Any], None]] = None,
        children: List[Union["UIElement", str]] = None,
    ):
        self.name = name
        self.props = props if props is not None else {}
        self.children = children if children is not None else []
        self.parent = None
        ctx = get_context()
        current_element = ctx.get("current_element")

        if current_element:
            current_element.add_child(self)
            self.parent = current_element

        self.key = self._generate_unique_key(key)
        
        default_state = init_default_state(
            key=self.key, default_value=default_value, **default_component_state
        )
        self.state = default_state
        self.default_state = default_state
        self.on_change = on_change

        st.session_state[self.key] = self.state

        init_element_state(self.key, self.default_state)

    def _generate_unique_key(self, key: Optional[str] = None) -> str:
        if key is not None:
            return key
        
        if self.parent is None:
            return self.name
        
        siblings = [child for child in self.parent.children if isinstance(child, UIElement) and child.name == self.name]
        index = siblings.index(self)
        return f"{self.parent.key}_{self.name}{index}"

    def render_tree(self, tree: Dict[str, Any]) -> Any:
        new_state = component_func(
            comp="element",
            props={"tree": tree},
            key=self.key,
            default=self.default_state,
        )
        
        if True or new_state != self.state:
            self._handle_state_change(new_state)
        
        return new_state

    def _handle_state_change(self, new_state: Dict[str, Any]) -> None:
        old_value = self.state.get("value")
        new_value = new_state.get("value")
        print("Old Value: ", old_value, self.on_change)
        # there are lots of on_change, we should trigger each one if it exists
        
        if True:# or old_value != new_value:
            if self.on_change:
                print("New Value: ", new_value)
                self.on_change(new_value)
            
            # Update the session state
            # st.session_state[self.key] = new_state
        
        self.state = new_state

    def render_props(self) -> Dict[str, Any]:
        children = []
        for child in self.children:
            if isinstance(child, UIElement):
                children.append(child.render_props())
            else:
                children.append(child)
        return {"name": self.name, "props": self.props, "children": children}

    def render(self) -> Any:
        return self.render_tree(self.render_props())

    def __enter__(self) -> "UIElement":
        ctx = get_context()
        ctx["current_element"] = self
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        ctx = get_context()
        if self.parent is None:
            self.render_tree(self.render_props())

        ctx["current_element"] = self.parent

    def add_child(self, child: Union["UIElement", str]) -> None:
        child.parent = self
        self.children.append(child)

    def __getattr__(self, item: str) -> Any:
        if item in self.props:
            return self.props[item]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{item}'"
        )

    @property
    def value(self) -> Any:
        return self.state["value"]

def element(
    name: str,
    *args,
    key: Optional[str] = None,
    default_value: Any = None,
    default_component_state: Any = {},
    on_change: Optional[Callable[[Any], None]] = None,
    **props,
) -> UIElement:
    children = []
    if on_change is not None:
        print("On Change is not None")
    for arg in args:
        if isinstance(arg, (UIElement, str)):
            children.append(arg)
        elif isinstance(arg, list):
            children.extend(arg)

    return UIElement(
        name=name,
        props=props,
        key=key,
        default_value=default_value,
        default_component_state=default_component_state,
        on_change=on_change,
        children=children if children else None,
    )

def text(
    value: str,
    key: Optional[str] = None,
    default_value: Any = None,
    default_component_state: Any = {},
    on_change: Optional[Callable[[Any], None]] = None,
    **props,
) -> UIElement:
    return element(
        "text",
        value,
        key=key,
        default_value=default_value,
        default_component_state=default_component_state,
        on_change=on_change,
        **props,
    )