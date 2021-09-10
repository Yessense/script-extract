from src.mapscript.preprocessing.extract_texts_info import extract_texts_info
from src.mapscript.script import Script
from src.mapscript.visualization.visualizator import Visualizator

filepath = 'my_text.txt'
text_info = extract_texts_info([filepath])[0]
script = Script(text_info)
vis = Visualizator(script, save_to_file=False)

vis.show()
print("Done")
