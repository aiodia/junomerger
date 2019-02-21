import pandas as pd
import numpy as np
import os
import io
from bs4 import BeautifulSoup
from urllib.request import urlopen
from IPython.core.display import display, HTML

class HTMLNotebook :
    def __init__(self, html_loc) :
        self.html_loc = html_loc
    
    #get jupyter notebook in html based on keyword
    def get_jupyter_output(self, keyword) :
        with io.open(self.html_loc, "r", encoding="utf-8") as f:
            page = f.read()
        page = BeautifulSoup(page, "html.parser")

        for div in page.find_all("div", {'class' : 'prompt'}) :
            div.decompose()

        element_list = page.find_all("div", class_="output_wrapper")

        error_message = "<h3>Not Found</h3>"

        for element in element_list :
            try :
                result = str(element)
                if keyword in result :
                    return(result)
            except ValueError :
                error_message = "<html><h3>Reaching arbitrary MAX_URI_LENGTH Limit</h3></html>"
        return(error_message)

    #directly show output from get_jupyter_output
    def show_jupyter_output(self, keyword) :
        result = self.get_jupyter_output(keyword)
        display(HTML(result))

#convert jupyter notebook into html
def convert_ipynb2html(notebook, new_file=None, verbose=False) :
    destination = notebook.replace('.ipynb', '.html') if new_file is None else new_file        
    command = "jupyter nbconvert {} --output {}".format(notebook, destination)
        
    if verbose :
        print(command)
        
    os.system(command)
    return(HTMLNotebook(destination))

    
#give hidden tag into jupyter output but hidden
def print_hidden_tag(text) :
    text_html = "<div style=\"display:none;\">{}</div>".format(text)
    display(HTML(text_html))