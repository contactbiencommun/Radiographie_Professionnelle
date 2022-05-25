import streamlit as st



def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

def getduplicat(a):
    import collections
    return [item for item, count in collections.Counter(a).items() if count > 1]

def getnotedispo(note_recupéré,note_total):
    templist=[]
    note_utilisé=list(set(note_recupéré))
    for elem in note_total:
      if elem not in note_utilisé:
        templist.append(elem)
    return templist


def insert_video(video1):
    """insert the video"""
    with st.container():
        video_file = open(video1, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)

def search2xelem(elem,tab):
    res=false



