import os
import spacy
from typing import Union
from spacy import displacy


class PDF(object):
    """Loads PDF file
    Args:
        object (object): PDF

    Returns:
        None: None
    """
    def __init__(self, pdf, size=(200,200)):
        self.pdf = pdf
        self.size = size

    def _repr_html_(self):
        return '<iframe src={0} width={1[0]} height={1[1]}></iframe>'.format(self.pdf, self.size)

    def _repr_latex_(self):
        return r'\includegraphics[width=1.0\textwidth]{{{0}}}'.format(self.pdf)

def load_model(modelname: str) -> spacy.ml:
    """Load spacy model

    Args:
        modelname (str): Model name
    """
    BASE_PATH = '../output/'
    modelpath = os.path.join(BASE_PATH+modelname)
    model = spacy.load(modelpath)
    print(f"\nLoaded {model.meta['lang'],model.meta['name']} model \n" )
    return model


def inference(model: spacy.ml, input_text: str, transformer=False) -> list:
    """Run inference

    Args:
        model (spacy.ml): Spacy model object, I guess
        input_text (str): Input inference text
        transformer (bool): Bool of transformer or not

    Returns:
        list: List of tuples which contains entities
    """
    doc = model(input_text)
    if (transformer==False):
        colors = {"Art ID": "linear-gradient(90deg, #aa9cfc, #fc9ce7)", "Price per unit": "linear-gradient(90deg, #b58ecc, #5de6de)"}
        options = {"ents": ["Art ID", "Price per unit"], "colors": colors}
    else:
        options = {}
    displacy.render(doc, style="ent", jupyter=True, options=options)
    return doc


def load_text(path: str, print_=False) -> Union[str, None]:
    """Load text file 

    Args:
        path (str): _description_
        print (bool, optional): _description_. Defaults to False.
    """
    with open(path) as f:
        content = f.readlines()
    content = content[0]
    if print_ == True:
        print(content)
    else:
        return content