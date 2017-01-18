import cv2
import math

import Image
import pytesseract

class GenerateHtml:

    added_html = ''

    def __init__(self):
        print "Created the object"

    def add_row(self, html):
        return "<div class='row'>" + html + "</div>";

    def on_same_level(self, prev, contour):
        curr_h = cv2.boundingRect(contour)[3]
        prev_h = cv2.boundingRect(prev)[3]

        if curr_h + 20 > prev_h and curr_h - 20 < prev_h:
            return True

        return False

    def append_html(self, contour, size, i, contours, img):
        block_type = self.recognize_type(contour, img)

        start_row = ""
        end_row = ""

        if i == 0:
            start_row = "<div class='row'>"
        elif i == (len(contours) - 1):
            end_row = "</div>"
        else:
            has_prev = self.on_same_level(contours[i-1], contour)
            has_next = self.on_same_level(contour, contours[i+1])

            if has_prev == True and has_next == False:
                end_row = "</div>"
            elif has_prev == False and has_next == True:
                start_row = "<div class='row'>"
            elif has_prev == False and has_next == False:
                start_row = "<div class='row'>"
                end_row = "</div>"



        if block_type == "div":
            GenerateHtml.added_html += start_row + "<div class=\"" + "col-md-" + str(size) + " standard-div\" " + "style=\"height: " + str(cv2.boundingRect(contour)[3] * 2) + "px;\"></div>\n" + end_row

    def recognize_type(self, contour, img):

        x, y, w, h = cv2.boundingRect(contour)

        croped_div = img[y:y + h, x:x + w]

        cv2.imwrite('./output/div' + str(y) + '.jpg', croped_div)

        print pytesseract.image_to_string(Image.open('./output/div' + str(y) + '.jpg'))

        return "div";

    def calculate_col(self, contour, width):
        rect = cv2.boundingRect(contour)

        one_col = width / 12

        return int(math.floor(rect[2] / one_col))



    def process_divs(self, img, contours):
        #find the largets outermost element and thats the size of the screen
        max_rectangle_index = self.biggest_rectangle(contours)

        max_rectangle = cv2.boundingRect(contours[max_rectangle_index])

        width = max_rectangle[2]
        height = max_rectangle[3]

        #remove the largest thats the window size
        del contours[max_rectangle_index]

        for i, c in enumerate(contours):
            size = self.calculate_col(c, width)
            self.append_html(c, size, i, contours, img)


    def biggest_rectangle(self, contours):
        contours_area = []

        for i, c in enumerate(contours):
            rect = cv2.boundingRect(c)
            contours_area.append(rect[2] * rect[3])

        return contours_area.index(max(contours_area))

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
