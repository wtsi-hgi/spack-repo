# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdpc(RPackage):
	"""One-Sided Dynamic Principal Components

	Functions to compute the one-sided dynamic
	principal components ('odpc') introduced in Peña, Smucler and Yohai (2019)
	<DOI:10.1080/01621459.2018.1520117>. 'odpc' is a novel dimension
	reduction technique for multivariate time series, that is useful
	for forecasting. These dynamic principal components are defined as
	the linear combinations of the present and past values of the series
	that minimize the reconstruction mean squared error.
	"""
	
	cran = "odpc" 

	version("2.0.5", md5="a269d19414d18ecf884377aaccc5476a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.500:", type=("build", "run"))
