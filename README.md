# Jupyter Notebook Merger

Simple library to merger several jupyter notebook into one


## Requirements

- Python 3.6
- [Pandas](https://pandas.pydata.org/) >= 0.23.4
- [Numpy](http://www.numpy.org) >= 1.15.1
- [beautifulsoup4 (bs4)](https://pypi.org/project/beautifulsoup4/) >= 4.5.1
- [urllib](https://docs.python.org/3/library/urllib.html)
- [IPython](https://ipython.org/) >= 6.5.0

## Getting Started

### Installing

Can be installed using [pip](https://pypi.org/project/pip/):

```sh
pip install git+git://github.com/aiodia/junomerger.git
```

### Usage

- import library
```sh
import junomerger
```
- Create several notebook, let say notebook A and B.
- Give unique keyword to several or all cell :
```sh
junomerger.print_hidden_tag('my_unique_keyword')
```
- Run notebook A and C, then save.
- Create notebook C to merge A and B
- Convert notebook A and B into html
```sh
notebook_a = junomerger.convert_ipynb2html('notebook_a.ipynb')
notebook_b = junomerger.convert_ipynb2html('notebook_b.ipynb')
```
- show particular output based on unique keyword has been created
```sh
notebook_a.show_jupyter_output(keyword='my_unique_keyword')
```

see this [articles]() and examples folder for details.

## License

This software is licensed with the MIT license. See `LICENSE.txt` for the full text.