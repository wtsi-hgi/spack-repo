# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWv(RPackage):
	"""Wavelet Variance

	Provides a series of tools to compute and plot quantities related to classical and robust wavelet variance for time series and regular lattices. More details can be found, for example, in Serroukh, A., Walden, A.T., & Percival, D.B. (2000) <doi:10.2307/2669537> and Guerrier, S. & Molinari, R. (2016) <arXiv:1607.05858>.  
	"""
	
	homepage = "https://github.com/SMAC-Group/wv"
	cran = "wv" 

	version("0.1.2", md5="da43a0ac251fa5712fe97ff068d730ed")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-simts", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
