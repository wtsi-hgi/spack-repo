# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectral(RPackage):
	"""Common Methods of Spectral Data Analysis

	On discrete data spectral analysis is performed by Fourier and Hilbert
    transforms as well as with model based analysis called Lomb-Scargle method.
    Fragmented and irregularly spaced data can be processed in almost all methods. Both,
    FFT as well as LOMB methods take multivariate data and return standardized PSD. 
    For didactic reasons an analytical approach for deconvolution of noise spectra and 
    sampling function is provided.
    A user friendly interface helps to interpret the results.
	"""
	
	cran = "spectral" 

	version("2.0", md5="aa299c0094d83a6eaf10069d84ef33a4")

	depends_on("r-rasterimage", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
