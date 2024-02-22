# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaselect(RPackage):
	"""Genetic Algorithm (GA) for Variable Selection from
High-Dimensional Data

	Provides a genetic algorithm for finding variable
    subsets in high dimensional data with high prediction performance. The
    genetic algorithm can use ordinary least squares (OLS) regression models or
    partial least squares (PLS) regression models to evaluate the prediction
    power of variable subsets. By supporting different cross-validation
    schemes, the user can fine-tune the tradeoff between speed and quality of
    the solution.
	"""
	
	homepage = "https://github.com/dakep/gaselect"
	cran = "gaselect" 

	version("1.0.22", md5="6af2be6392304399be4c82bd188f8746")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp@0.10.5:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.9.800.4:", type=("build", "run"))
