import pandas

def load(path: str) :
    try :
        cvs = pandas.read_cvs(path)
        print(f"Loading dataset of dimensions {cvs.shape}")
        return cvs
    except Exception as e :
        return None