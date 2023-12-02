import numpy as np
import math
import matplotlib.pyplot as plt

DPI = 10

def show(
    image,
    ax=None,
    rotate=False,
    scale=1,
    title=None,
    fontsize=10,
    cmap=None,
    return_ax=False,
):
    h, w = image.shape[:2]
    if ax is None:
        fig, ax = plt.subplots(figsize=(int(scale * h), int(scale * w)), dpi=DPI)
    ax.cla()
    ax.axis("off")
    if rotate:
        param = (1, 0) if image.ndim == 2 else (1, 0, 2)
        image = np.transpose(image, param)[::-1]
    ax.imshow(image, cmap=cmap)
    if title:
        ax.set_title(title, fontsize=DPI * fontsize)
    if return_ax:
        return ax


def show_collection(
    images,
    titles=[],
    num_rows=-1,
    num_cols=-1,
    scale=1,
    cmap=None,
    return_axes=False,
    fontsize=10,
    # pad=1.0,
):
    assert len(images) > 1

    if num_cols == -1:
        # none provided: fix row in 1
        if num_rows == -1:
            num_rows = 1
        # compute #cols based on #rows
        num_cols = len(images) // num_rows
    else:
        # only #cols provided: fix cols, compute rows
        if num_rows == -1:
            num_rows = math.ceil(len(images) / num_cols)
        # both rows and cols provided: fix rows, compute cols
        else:
            num_cols = math.ceil(len(images) / num_rows)

    if len(titles) > 0:
        assert len(titles) == len(images)
    else:
        titles = len(images) * [""]

    h, w = images[0].shape[:-1] if images[0].ndim == 3 else images[0].shape
    fig, axes = plt.subplots(
        nrows=num_rows,
        ncols=num_cols,
        figsize=(int(scale * w * num_cols), int(scale * h * num_rows)),
        dpi=DPI,
    )
    k = 1
    for ax, image, title in zip(axes.flatten(), images, titles):
        ax.imshow(image, cmap=cmap)
        ax.axis("off")
        ax.set_title(title, fontsize=DPI * fontsize)
        k += 1
    fig.tight_layout()
    if return_axes:
        return axes
