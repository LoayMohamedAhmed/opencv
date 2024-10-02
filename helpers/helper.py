from matplotlib import pyplot as plt

def plot(images , titles, figsize ,filter,suptitle =""):
    imag_no = len(images)
    # r and c are the number of rows and columns in the plot
    if imag_no%2 == 0 and imag_no>2:
        r = c = int(imag_no/2)
    else:
        r = 1
        c = imag_no

    plt.figure(figsize= figsize)
    plt.suptitle(suptitle)
    for i in range(len(images)):
        plt.subplot(r,c,i+1)
        plt.title(titles[i])
        if filter and i!=0:
            cmap = 'gray'
        else:
            cmap = None
        plt.imshow(images[i],cmap=cmap)
        plt.xticks([]), plt.yticks([])
    plt.show()
