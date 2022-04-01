from tensorflow.keras.datasets import mnist # pylint: disable=E0611, E0401
from dataset import image_processing
from distance import mhd

# NOTE: Importing the mnist database takes about 7-10 seconds
# the program itself runs in about 1.5 seconds.

(x_train, y_train), (x_test, y_test) = mnist.load_data()

def main():
    training_images = image_processing.sort_images_and_threshold(x_train, y_train, True)
    testing_images = image_processing.sort_images_and_threshold(x_test, y_test, False)
    edge_training_set = image_processing.create_binary_edge_image(training_images)
    edge_testing_set = image_processing.create_binary_edge_image(testing_images)
    #image_processing.print_training_image(edge_testing_set)
    print(edge_training_set.shape)
    print(edge_testing_set.shape)
    print(image_processing.coordinates(edge_testing_set[0]).shape)
    print(mhd.mhd_d22(edge_testing_set[0], edge_training_set[4532]))
    #print(edge_testing_set[0])
    #print(edge_training_set[4532])

if __name__ == "__main__":
    main()
