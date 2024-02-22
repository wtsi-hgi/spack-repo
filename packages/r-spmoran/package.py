# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpmoran(RPackage):
	"""Fast Spatial Regression using Moran Eigenvectors

	Functions for estimating spatial varying coefficient models, mixed models, and other spatial regression models for Gaussian and non-Gaussian data. Moran eigenvectors are used to an approximate spatial Gaussian processes. These processes are used for modeling the spatial processes in residuals and regression coefficients. For details see Murakami (2021) <arXiv:1703.04467>.
	"""
	
	cran = "spmoran" 

	version("0.2.3", md5="6e3ec978c3b98b791d0decba89b2d18f")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
