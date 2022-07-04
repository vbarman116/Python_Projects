import json
import os


class MadLibs:
    path = 'Python_Projects/Project_1_Easy/Mad_Libs/templates'
    def __init__(self, word_descriptions, template):
        self.word_descriptions = word_descriptions
        self.template = template
        self.user_input = []
        self.story = None

    @classmethod
    def from_json(cls, name, path = None):
        if not path:
            path = cls.path
        fpath = os.path.join(path , name)
        # print(os.path.exists(fpath))
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_lib = MadLibs(**data)
        return mad_lib
  

    def get_words_from_user(self):
        print("Please provide the following words: ")
        for word_desc in self.word_descriptions:
            UI = input(word_desc + " ")  #UI = user inputs
            self.user_input.append(UI)
        return self.user_input

    def Building_the_story(self):
        self.story = self.template.format(*self.user_input)
        return self.story

    def show_story(self):
        print(story)

def select_templates():
    print("Select a Mad Lib from the following list:")
    templates = os.listdir(MadLibs.path)    
    template = input(str(templates) + " ")
    return template
    
temp_name = select_templates()  
# temp_name = "day_at_the_zoo.json"
mad_lib = MadLibs.from_json(temp_name)
words = mad_lib.get_words_from_user()
story = mad_lib.Building_the_story()
mad_lib.show_story()