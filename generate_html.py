import cv2
import math

class GenerateHtml:

    added_html = ''

    def __init__(self):
        print "Created the object"

    def add_row(self, html):
        return "<div class='row'>" + html + "</div>";

    def append_html(self, contour, size):
        block_type = self.recognize_type(contour)

        if block_type == "div":
            GenerateHtml.added_html += "<div class='row'><div class=\"" + "col-md-" + str(size) + " standard-div\" " + "style=\"height: " + str(cv2.boundingRect(contour)[3]) + "px;\"></div>\n</div>\n"

    def recognize_type(self, contour):
        return "div";

    def calculate_col(self, contour, width):
        rect = cv2.boundingRect(contour)

        one_col = width / 12

        return int(math.floor(rect[2] / one_col))



    def process_divs(self, contours):
        #find the largets outermost element and thats the size of the screen
        max_rectangle = cv2.boundingRect(contours[5])

        print max_rectangle

        width = max_rectangle[2]
        height = max_rectangle[3]

        #remove the largest thats the window size
        contours.pop()

        for c in contours:
            size = self.calculate_col(c, width)
            self.append_html(c, size)


    def write_html(self, name):
        html_file = open("output/" + name + ".html", "wb")

        html_file.write("""
            <!DOCTYPE html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <title>Bootstrap 101 Template</title>

                <link href="bootstrap.min.css" rel="stylesheet">
                <link href="custom.css" rel="stylesheet">

              </head>
              <body>
                <div class="container">
                <h2>Ouh look we generated a site for you</h2>
                """ + GenerateHtml.added_html + """
                </div>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
                <script src="bootstrap.min.js"></script>
              </body>
            </html>
            """)

        html_file.close()
