import matplotlib.pyplot as plt

def show_image(image, title=None):
    plt.imshow(image, interpolation='nearest')
    if title is not None:
        plt.title(title)
    plt.show()

def compare_image(image1, image2, title=None):
    fig = plt.figure()
    ax1 = fig.add_subplot(1,2,1)
    ax1.imshow(image1, interpolation='nearest')
    ax2 = fig.add_subplot(1,2,2)
    ax2.imshow(image2, interpolation='nearest')
    if title is not None:
        plt.title(title)
    plt.show()