# DrawAWebsite
*Project for Soft computing course where html is generated from a sketch*

## How to run?
You need to have python 2.7 installed alongside with opencv installed on the system

Run the app with ``` python main.py```

## Idea
The main idea of the app is that the user will draw a sketch mockup of a website, take the picture of that and the app will generate html based on the users sketch.

This will only support basic html items and simple layout format.

## Specification
  **How the sketch should be drawn?**

The sketch should be very clear with thick lines so it can be easily scanned. Each element should be drawn as a rectangle (box) and depending on specific markers the app will differentiate between (div, button, input...).

The markers might change but currently the way you would draw a button will be a box with a string 'Button' in it an input box would have letter 'Input' etc. so letters are markers for which ui control your box is.

The text you draw must be big and readable based on the text size it will be determined if text font size.


  **Basic tags/elements we need to support**
  * ``` <h1> </h1> different size header tags```
  * ``` Buttons ```
  * ``` Input boxes```
  * ``` Lists (ordered and unordered) ```
  * ``` Checkbox```
  * ``` Selectboxes ```
  * ``` Images ```
  * ``` Footer ```
  * ``` Divs of different sizes ```

All the elements will use Bootstrap to generate nice looking elements and different layout. Using bootstraps box grid layout to estimate the size of boxes that are drawn in the sketch.

The app should also support coloring different elements, so the user will add color to a certain box (div) and it will generate css to color it.


## Technology
* Python 2.7
* Opencv
* Bootstrap 3.0
