import matplotlib.pyplot as plt


def method_temp_range_bar(methods):
    figure = plt.figure()
    axes = figure.add_subplot(1,1,1)
    axes.bar(range(len(methods)), tick_label = [methods[0] for method in methods])
        
    
    plt.show()
