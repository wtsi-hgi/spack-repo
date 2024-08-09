# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignal(RPackage):
    """Signal Processing

    A set of signal processing functions originally written for 'Matlab' and 'Octave'.
  Includes filter generation utilities, filtering functions,
  resampling routines, and visualization of filter models. It also
  includes interpolation functions.
    """
    
    cran = "signal" 

    version("1.8-1", sha256="a322bc13c2d3ff43a7f24970e52277d3d8ebc47fdaa9f63e210ed53655e1eeb0")
    version("1.8-0", sha256="0a604949bae91410a150a22cfa02d954f5b83166cc7a73e5409554d00e0417a7")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
