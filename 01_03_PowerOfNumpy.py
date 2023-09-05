import numpy as np
import time

def test_run():
    a = np.random.normal(50,10,size=(2,3))
    print(a.shape[0]) # number of Rows
    print(a.shape[1]) # number of columns
    print(a.size) # Number of Element in a
    print(a.dtype) # Gets the data type of the elements

def test_math():
    np.random.seed(693)
    a = np.random.randint(0, 10, size=(5,4))
    print(f"Sum of all elements: {a.sum()}")
    print(f"Sum of each column: {a.sum(axis=0)}")
    print(f"Sum of each row: {a.sum(axis=1)}")
    print(f"Minimum of each columns: {a.min(axis=0)}")
    print(f"Minimum of each rows: {a.min(axis=1)}")
    print(f"Mean of all elements: {a.mean()}")
    b = np.array([1,4,5,9,10,2,3,15,10,2,3])
    print(f"Index of Max Index: {get_max_index(b)}")

def access_elements():
    a = np.random.rand(5,4)
    print(a)

    # Elements in a defined range
    element = a[0,1:3]
    # Prints all rows and Every other column
    print(a[:,0:3:2])

def numpy_indexing():
    a = np.random.rand(5)

    indicies = np.array([1,1,2,3])

    print(a)
    # Prints the values at the indicies array
    print(a[indicies])

def boolean_arrays():
    a = np.array([(20,25,10,23,26,32,10,5,0), (0,2,50,20,0,1,28,5,0)])
    print(a)

    mean = a.mean()
    print(mean)

    # Get all the values that are less than the mean in the ndarray
    print(a[a<mean])

    # Replace all the items in the array less than the mean with the mean
    a[a<mean] = mean
    print(a)

def get_max_index(a):
    return a.argmax()


if __name__ == "__main__":
    boolean_arrays()