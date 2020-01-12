# Dash HTML Nesting 

## Line 6

A common pattern for creating layouts in Dash apps is to  create a top-level `html.Div()` component whose `children` are themselves components. 

In this example, the top-level `html.Div()` component has two `children` components: an `html.H1()` component and another `html.Div()` component. 

Note the use of Python list to pass multiple components as `children` paraments to the top-level component. 