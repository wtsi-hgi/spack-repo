# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShiftconvolvepoibin(RPackage):
	"""Exactly Computing the Tail of the Poisson-Binomial Distribution

	An exact method for computing the Poisson-Binomial Distribution (PBD). The package provides a function for generating a random sample from the PBD, as well as two distinct approaches for computing the density, distribution, and quantile functions of the PBD. The first method uses direct-convolution, or a dynamic-programming approach which is numerically stable but can be slow for a large input due to its quadratic complexity. The second method is much faster on large inputs thanks to its use of Fast Fourier Transform (FFT) based convolutions. Notably in this case the package uses an exponential shift to practically guarantee the relative accuracy of the computation of an arbitrarily small tail of the PBD -- something that FFT-based methods often struggle with. This ShiftConvolvePoiBin method is described in Peres, Lee and Keich (2020) <arXiv:2004.07429> where it is also shown to be competitive with the fastest implementations for exactly computing the entire Poisson-Binomial distribution.
	"""
	
	cran = "ShiftConvolvePoibin" 

	version("1.0.0", md5="2d6aadd0a5a76f53b8fa0ee7d3dbff18")

