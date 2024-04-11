import base64 


with open("food.jpeg", "rb") as image2string: 
	converted_string = base64.b64encode(image2string.read()) 
print(converted_string) 

with open('encode.bin', "wb") as file: 
	file.write(converted_string)

retval, buffer = cv2.imencode('.jpg', image)
jpg_as_text = base64.b64encode(buffer).decode()


<div>20240328202412[0] <img src="data:image/jpeg;base64, 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"> Cold Protection</div>
427 265200 Cold Protection
<div>20240328202412[1] <img src="data:image/jpeg;base64, /9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAIBAQEBAQIBAQECAgICAgQDAgICAgUEBAMEBgUGBgYFBgYGBwkIBgcJBwYGCAsICQoKCgoKBggLDAsKDAkKCgr/wAALCAA4ADgBAREA/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/9oACAEBAAA/AP38ooooooooorx/xl+3r+yd8P8A9snwn/wT98XfFb7J8XfHPh+TW/C3hL+wr+T7bYRpeu832pIDax4XT7w7ZJVY+TwPnTd7BRRRXP8AxZ+KXgT4HfCzxN8a/ilrv9l+GPB/h+91vxHqf2WWf7JYWkDz3E3lwq8kmyKN22orM2MKCSBX54P/AMFZ/wBmD/gp9+1xB/wTg+Gnx18H6/8AAf8AaM/Zw8UaZpXiHwwZo/F0fihJbm21Cwltpy0mlRLpAmu4ZL+xjSd0zFLMP3R/LD4dfsff8FkvF/8Awchv+zf4Z/b1/wCEg+LvwS8P28LfHbxHaQ6imieDTpdvAl0NPv1dZ7l7TV40e2HmGS+vZpZLht01/X7P/sbf8FNvhZcfHbxD+xTrvjvw/a+CfhX4gt/hR4N+LfxU+MsA8VfE/wAZada6bDqNlFpdzaQTXdzBNdpHcXayETzzwNAkq3DGH7foorx//goH4I8CfEL9h34s+GfiT+zf/wALg0j/AIV/ql3J8L0WXzvE01tbPcwWNu0KSTRXMk0UQhmhRpopvLkiHmIlfgDpf/BrB+1P4T8CfFH/AIKF/FD42eH/ANkyDwT/AGv44+HfgTTtUvvFN/4RtrGW8vIIbzVrB/Mh+zRW9q0d3aC+uHVjIYlmTyX+IP8Agmxpv/BRL/goH/wUEPhP4A/8FB/EHgv42+PfD91Cvj7xT8RfEFrf+IYbO3jnfT5dRsIrm4bFtZCVVnKw7bBV371hRv0v/wCCZv8Awby6j+wz/wAFafBfhT9sr9mT4oeO9K0fxhf698Jfjr4C8Q2//CHSyabbQXtgdc02O3a80qVZQ7K0t6sc13HFbJDdwCad/wCg6iiuP/aF+HHir4x/ALxx8IvAvxO1DwTrfirwfqej6N4z0kObrQLq5tZIYtQh8uWJ/Ngd1lXbJG26MYdD8w/ky/4KS+NP2p/iJrHxc+En7L//AAUA/aA/aH+AXwc8P6BD8XviH4u+K19qXhvWtVlvLWA3UNtKUhjtn1SRYrS233ruLKS7juJ4VMkX1/8A8HNv7C3gT9kbWP2VvA3/AATt8GeID42+C3wf1W71/U/BLSvreh+G9GvLOey8R30enKi2P/EwutWuZNTEUAluZJ3aQtGAn6H/APBuH48/bC/ab/Zf8KftafFz/gqjqHxk8G3Pg+Xw3dfC/XPhtpFnqfhfX7Sa3jZ7zVrW5mu7yVYYnZDdbZbmDUILqVUdwtfpfRRRXyB8Q/8Aghd/wTj8UfsnfFr9jr4Y/Br/AIVh4Y+NfiCz1nx5ffDyWO3v5rm1v4b6COB7uO4jtraOWHEdpHGLeFZphDFEZWY+n+LP+CfvwC8e/toan+2746g1DWtb1r4HzfCnWfCWrLa3OgX+gTaib+UTWskBeWV3ZomDSGJomKmIk7q6D9kP9i/9mD9gv4NQfAD9kf4Qaf4L8KQ6hPftp9lPNPJc3UxBkuJ7i4eSe5lIVEDyu7LHFFGpCRoq+oUUUUUUUUV//9k="> B Cold Protection</div>
427 265200 Cold Protection
427 259080 Life Support



what css style do I apply to this div to center the text and image horizontally? do I need to put the text in a span?

<div>20240328202412[3] A <img src="data:image/jpeg;base64, ..."> Hot Protection</div>


when I run main1.py, tech.html is empty. How do I fix this?

# main1.py

import mod1.py
html_page = []
mod1.set_page(html_page)
with open(f'tech.html', 'w') as outfile:
  outfile.write(html_page)



# mod1.py

def set_html(html_page):
for n in range(10):
	html_page.append(f'{n}<br>')








# Define a variable at the module level
work_image = None

# Define a function that accesses the variable
def process_image():
    # Access the global variable without using 'this.'
    global work_image
    if work_image is None:
        print("No image to process")
    else:
        print("Processing image:", work_image)

# Define a function that modifies the variable
def set_image(image, html_page):
    # Access the global variable without using 'this.'
    global work_image
    work_image = image
    print("Image set to:", work_image)
    html_page += 'some text to append'

