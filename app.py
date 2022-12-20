from jinja2 import Template
from flask import Flask
TEMPLATE="""hello {{name}}"""
def main():
  template=Template(TEMPLATE)
  print(render.template(name="eswar"))
if __name__=="__main__":
  main()
