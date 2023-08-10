import face_recognition as fr
import numpy as np
import pickle


# Returns how many encodings and the encodings as a tuple
# from the image provided
def encodeFace(img_path, path=False):
    if path:
        load_img= fr.load_image_file(img_path)
    else:
        load_img= img_path
    
    face_dims= fr.face_locations(load_img)
    encodings= fr.face_encodings(load_img, face_dims)

    return len(encodings), encodings, face_dims


# loads the list of encodes into the given source
def save_encodings(arr, source):
    with open(source, 'wb') as f:
        pickle.dump(arr, f)

# deloads the ecodes from a sources into a list
def get_encodings(source):
    with open(source, 'rb') as f:
        arr= pickle.load(f)
    return arr

# x is number of unique potraits you have
# 5 should be good enough
def encode_faces(x):

    encode_list= []
    for i in range(1, x+1):
        img_path= 'yourname/{}.png'.format(i)

        len, encode, dims= encodeFace(img_path, path=True)
        if len:
            encode_list.append(encode)
        
    save_encodings(encode_list, 'myencodings.dat')

# Returns true if the test_img matches with given encodings
def compareFace(img_encodings, test_img_encode, tol=0.1):
    
    for encode in test_img_encode:
        for known_encode in img_encodings:
            match= fr.compare_faces([known_encode], encode, tol)

            if np.all(match):
                return True

    return False

if __name__ == "__main__":

    x= input("How many photos are in the 'yourfaces' folder?: " )

    encode_faces(int(x))
