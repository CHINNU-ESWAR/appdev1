from jinja2 import Template
from flask import Flask
data_set=[
{"year":2000,"awardee":"abcs","state":"andhra]
def main():
  template_file=open("extemplate.jinja2",'r')
  TEMPLATE=template_file.read()
  template_file.close()
  template=Template(TEMPLATE)
  print(template.render(data_set=data_set))
if __name__=="__main__":
  main()
