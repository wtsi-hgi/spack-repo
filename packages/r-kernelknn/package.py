# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKernelknn(RPackage):
	"""Kernel k Nearest Neighbors

	Extends the simple k-nearest neighbors algorithm by incorporating numerous kernel functions and a variety of distance metrics. The package takes advantage of 'RcppArmadillo' to speed up the calculation of distances between observations.
	"""
	
	homepage = "https://github.com/mlampros/KernelKnn"
	cran = "KernelKnn" 

	version("1.1.5", md5="1f67b9a401d36132a78e36f09bbe8be2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("armadillo", type=("build", "link", "run"))
	depends_on("lapack", type=("build", "link", "run"))
	depends_on("blas", type=("build", "link", "run"))
	depends_on("arpack-ng", type=("build", "link", "run"))
	depends_on("gcc", type=("build", "link", "run"))
