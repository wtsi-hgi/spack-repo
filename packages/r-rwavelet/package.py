# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwavelet(RPackage):
	"""Wavelet Analysis

	Perform wavelet analysis (orthogonal,translation invariant, tensorial, 1-2-3d transforms, thresholding, block thresholding, linear,...) with applications to data compression or denoising/regression. The core of the code is a port of 'MATLAB' Wavelab toolbox written by D. Donoho, A. Maleki and M. Shahram (<https://statweb.stanford.edu/~wavelab/>).
	"""
	
	homepage = "https://github.com/fabnavarro/rwavelet"
	cran = "rwavelet" 

	version("0.4.1", md5="9512da6364b38a7ba3993a3300755ea9")

	depends_on("r-signal", type=("build", "run"))
