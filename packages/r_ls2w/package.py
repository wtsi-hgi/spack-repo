# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLs2w(RPackage):
	"""Locally Stationary Two-Dimensional Wavelet Process Estimation
Scheme

	Estimates two-dimensional local wavelet spectra.
	"""
	
	cran = "LS2W" 

	version("1.3.6", md5="0b4014899a51db7e97c55847b8c8dfdd")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-wavethresh@4.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
