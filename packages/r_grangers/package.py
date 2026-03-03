# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrangers(RPackage):
	"""Inference on Granger-Causality in the Frequency Domain

	Contains five functions performing the calculation of unconditional and conditional Granger-causality spectra, bootstrap inference on both, and inference on the difference between them via the bootstrap approach of Farne' and Montanari, 2018 <arXiv:1803.00374>.
	"""
	
	homepage = "https://github.com/MatFar88/grangers"
	cran = "grangers" 

	version("0.1.0", md5="4924c3d9bb43c2c2c379d290e0939a2a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
