import matplotlib
import matplotlib.pyplot as plt

def visualize_anchors(anchors,
        grid_size = None
        ):
    f,ax = plt.subplots(1)
    for a in anchors:
        r = matplotlib.patches.Rectangle((a.bottomleft.x,
                a.bottomleft.y),
                a.width,
                a.height,
                ec='red',
                fill=False)
        #import pdb;pdb.set_trace()
        ax.add_patch(r)
    plt.axis('scaled')
    plt.show()

pass
