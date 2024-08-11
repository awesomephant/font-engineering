from fontTools import ttLib
import fontTools.feaLib
import fontTools.feaLib.builder
import fontTools.merge
from fontTools.pens.ttGlyphPen import TTGlyphPen

from string import Template
from os import listdir
from os.path import isfile, join

input_dir = "./input/"
output_dir = "./output/"

input_files = [f for f in listdir(input_dir) if isfile(join(input_dir, f)) and ".ttf" in f]

names_file = open("./names.txt", "r")
names = [n.replace("\n", "") for n in names_file.readlines()]

print(str(len(input_files)) + " input files found")
print(str(len(names)) + " names found")

def to_glyphname(s):
    dictionary = {
        ",": "comma",
        " ": "space",
        "1":"one",
        "2":"two",
        "3":"three",
        "4":"four",
        "5":"five",
        "6":"six",
        "7":"seven",
        "8":"eight",
        "9":"nine"
    }
    return dictionary[s] if s in dictionary else s

glyphs = []
for i, name in enumerate(names):
    for j, letter in enumerate(list(name)):
        glyphs.append(to_glyphname(letter))
        if (i < len(names) - 1 and j == len(name) - 1):
            glyphs.append(to_glyphname(","))
            glyphs.append(to_glyphname(" "))

fea = Template("feature liga {\
        sub [m M] [a A] [d D] [u U] [r R] [o O] by n_a_m_e_s;\
        sub n_a_m_e_s' by ${names};\
    } liga;").substitute(names=" ".join(glyphs))


for input_file in input_files:
    input_path = input_dir + input_file
    filename = input_file.replace(".ttf", "")
    tt = ttLib.TTFont(input_path)
    
    ttPen = TTGlyphPen(None)
  
    tt["glyf"]["n_a_m_e_s"] = ttPen.glyph()
    tt["hmtx"]["n_a_m_e_s"] = (100, 0)
    
    fontTools.feaLib.builder.addOpenTypeFeaturesFromString(tt, fea)

    output_path = "./output/" + filename + "-modified.ttf"
    tt.save(output_path)
    print("Saved " + output_path)