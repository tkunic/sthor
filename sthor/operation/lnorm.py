"""Local Normalization Operations"""

# Authors: Nicolas Pinto <nicolas.pinto@gmail.com>
#          Nicolas Poilvert <nicolas.poilvert@gmail.com>
#
# License: BSD

__all__ = ['lcdnorm3']

import numpy as np

from skimage.util.shape import view_as_windows
from sthor.util.pad import pad2d

EPSILON = 1e-4
DEFAULT_STRIDE = 1
DEFAULT_THRESHOLD = 1.0
DEFAULT_STRETCH = 1.0
DEFAULT_CONTRAST = True
DEFAULT_DIVISIVE = True


def lcdnorm3(arr_in, neighborhood,
             mode='valid',
             pad_val=0.,
             contrast=DEFAULT_CONTRAST,
             divisive=DEFAULT_DIVISIVE,
             stretch=DEFAULT_STRETCH,
             threshold=DEFAULT_THRESHOLD,
             stride=DEFAULT_STRIDE, arr_out=None):
    """3D Local Contrast Divisive Normalization

    XXX: docstring
    """

    assert arr_in.ndim == 3
    assert len(neighborhood) == 2
    assert isinstance(contrast, bool)
    assert isinstance(divisive, bool)
    assert contrast or divisive

    # -- mode check
    supported_modes = ['valid', 'same']
    if mode.lower() not in supported_modes:
        raise ValueError('mode "%s" not supported' % mode)

    # -- if mode == 'same', we pad the tensor with a
    #    constant value along the first two directions
    if mode.lower() == 'same':
        arr_in = pad2d(arr_in, neighborhood, pad_val)

    inh, inw, ind = arr_in.shape

    nbh, nbw = neighborhood
    assert nbh <= inh
    assert nbw <= inw

    nb_size = 1. * nbh * nbw * ind

    if arr_out is not None:
        assert arr_out.dtype == arr_in.dtype
        assert arr_out.shape == (inh - nbh + 1, inw - nbw + 1, ind)

    # -- prepare arr_out
    lys = nbh / 2
    lxs = nbw / 2
    rys = (nbh - 1) / 2
    rxs = (nbw - 1) / 2
    _arr_out = arr_in[lys:inh-rys, lxs:inw-rxs]

    # -- Contrast Normalization
    if contrast:

        # -- local sums
        arr_sum = arr_in.sum(-1)
        arr_sum = view_as_windows(arr_sum, (1, nbw)).sum(-1)[:, ::stride, 0]
        arr_sum = view_as_windows(arr_sum, (nbh, 1)).sum(-2)[::stride, :]

        # -- remove the mean
        _arr_out = _arr_out - arr_sum / nb_size

    # -- Divisive (gain) Normalization
    if divisive:

        # -- local sums of squares
        arr_ssq = (arr_in ** 2.0).sum(-1)
        arr_ssq = view_as_windows(arr_ssq, (1, nbw)).sum(-1)[:, ::stride, 0]
        arr_ssq = view_as_windows(arr_ssq, (nbh, 1)).sum(-2)[::stride, :]

        # -- divide by the euclidean norm
        if contrast:
            l2norms = (arr_ssq - (arr_sum ** 2.0) / nb_size)
        else:
            l2norms = arr_ssq

        #l2norms = l2norms.clip(0, np.inf)
        #val = l2norms.copy()
        np.putmask(l2norms, l2norms < 0., 0.)
        l2norms = np.sqrt(l2norms) + EPSILON
        #l2norms = np.sqrt(l2norms)

        if stretch != 1:
            _arr_out *= stretch
            l2norms *= stretch

        # XXX: use numpy-1.7.0 copyto()
        #np.putmask(l2norms, l2norms < (threshold + stretch * EPSILON), 1.0)
        np.putmask(l2norms, l2norms < (threshold + EPSILON), 1.0)
        #np.putmask(l2norms, l2norms < threshold, 1.0)

        #print 'XXX', l2norms.mean()

        #import IPython; ipshell = IPython.embed; ipshell(banner1='ipshell')

        # -- avoid zero division
        #np.putmask(l2norms, l2norms < EPSILON, EPSILON)

        _arr_out = _arr_out / l2norms

    if arr_out is not None:
        arr_out[:] = _arr_out
    else:
        arr_out = _arr_out

    assert arr_out.dtype == arr_in.dtype  # XXX: should go away

    return arr_out

try:
    lcdnorm3 = profile(lcdnorm3)
except NameError:
    pass
