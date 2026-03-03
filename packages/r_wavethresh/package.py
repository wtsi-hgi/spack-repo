# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWavethresh(RPackage):
	"""Wavelets Statistics and Transforms

	Performs 1, 2 and 3D real and complex-valued wavelet transforms,
	nondecimated transforms, wavelet packet transforms, nondecimated
	wavelet packet transforms, multiple wavelet transforms,
	complex-valued wavelet transforms, wavelet shrinkage for
	various kinds of data, locally stationary wavelet time series,
	nonstationary multiscale transfer function modeling, density
	estimation.
	"""
	
	cran = "wavethresh" 

	version("4.7.2", md5="1e88d73de0dfee4283b44f474c50b427")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
