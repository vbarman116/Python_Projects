'''
Hello Everyone this is the easiest way to build a MadLib Generator 
with the help of jinja2    
'''

from jinja2 import Environment, FileSystemLoader 
env = Environment(loader=FileSystemLoader('Python_Projects/Project_1_Easy/Mad_Libs_Using_Jinja2/templates')) #path location where you saved all the templates
template =  env.get_template('Second_Template.txt') #the template you have to use
output = template.render(noun = "Zoo", Animal = "Giraffe" , adverb = "Big", verb = "eating") #and for the render you know where to add the values as per jinja2 syntax
print(output)