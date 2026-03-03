# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWavelets(RPackage):
	"""Functions for Computing Wavelet Filters, Wavelet Transforms and
Multiresolution Analyses

	Contains functions for computing and plotting
        discrete wavelet transforms (DWT) and maximal overlap discrete
        wavelet transforms (MODWT), as well as their inverses.
        Additionally, it contains functionality for computing and
        plotting wavelet transform filters that are used in the above
        decompositions as well as multiresolution analyses.
	"""
	
	cran = "wavelets" 

	version("0.3-0.2", md5="c0453ddfb2fddeb2e09e9f3a3babdf11")

	depends_on("r@2.10:", type=("build", "run"))
