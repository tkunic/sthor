"""Local Pooling Operations"""

# Authors: Nicolas Pinto <nicolas.pinto@gmail.com>
#          Nicolas Poilvert <nicolas.poilvert@gmail.com>
#
# License: BSD

__all__ = ['lpool3']

import numpy as np
from skimage.util.shape import view_as_windows
from sthor.util.pad import pad2d

import numexpr as ne
if not ne.use_vml:
    import warnings
    warnings.warn("numexpr is NOT using Intel VML!")

# --
DEFAULT_STRIDE = 1
DEFAULT_ORDER = 1.0


def lpool3(arr_in, neighborhood,
           mode='valid',
           pad_val=0.,
           order=DEFAULT_ORDER,
           stride=DEFAULT_STRIDE, arr_out=None):
    """3D Local Pooling Operation

    XXX: docstring
    """
    assert arr_in.ndim == 3
    assert len(neighborhood) == 2

    order = np.array([order], dtype=arr_in.dtype)
    stride = np.int(stride)

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

    if arr_out is not None:
        assert arr_out.dtype == arr_in.dtype
        assert arr_out.shape == ((inh - nbh + 1) / stride,
                                 (inw - nbw + 1) / stride,
                                 ind)

    _arr_out = ne.evaluate('arr_in ** order')
    _arr_out = view_as_windows(_arr_out, (1, nbw, 1))
    _arr_out = ne.evaluate('sum(_arr_out, 4)')[:, ::stride, :, 0, 0]
    _arr_out = view_as_windows(_arr_out, (nbh, 1, 1))
    _arr_out = ne.evaluate('sum(_arr_out, 3)')[::stride, :, :, 0, 0]
    # Note that you need to use '1' and not '1.0' so that the dtype of
    # the exponent does not change (i.e. get promoted)
    _arr_out = ne.evaluate('_arr_out ** (1 / order)')

    if arr_out is not None:
        arr_out[:] = _arr_out
    else:
        arr_out = _arr_out

    assert arr_out.dtype == arr_in.dtype

    return arr_out

try:
    lpool3 = profile(lpool3)
except NameError:
    pass

