# coding: utf-8
from __future__ import absolute_import, division, print_function

import astropy.units as u
import numpy as np

from astrodynamics.compat.math import isclose
from astrodynamics.rotation import normalize_angle


def check_vector(v1, v2, rtol=0, atol=1e-15):
    assert np.allclose(v1, v2, rtol=rtol, atol=atol)


def check_rotation(r1, r2, rtol=0, atol=1e-15):
    assert isclose(r1.q0, r2.q0, rel_tol=rtol, abs_tol=atol)
    assert isclose(r1.q1, r2.q1, rel_tol=rtol, abs_tol=atol)
    assert isclose(r1.q2, r2.q2, rel_tol=rtol, abs_tol=atol)
    assert isclose(r1.q3, r2.q3, rel_tol=rtol, abs_tol=atol)


def check_angle(a1, a2, rtol=0, atol=1e-12 * u.rad):
    assert np.isclose(
        a1, normalize_angle(a2, center=a1), rtol=rtol, atol=atol)