# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixture(RPackage):
	"""Mixture Models for Clustering and Classification

	An implementation of 14 parsimonious mixture models for model-based clustering or model-based classification. Gaussian, Student's t, generalized hyperbolic, variance-gamma or skew-t mixtures are available. All approaches work with missing data. Celeux and Govaert (1995) <doi:10.1016/0031-3203(94)00125-6>, Browne and McNicholas (2014) <doi:10.1007/s11634-013-0139-1>, Browne and McNicholas (2015) <doi:10.1002/cjs.11246>.
	"""
	
	cran = "mixture" 

	version("2.1.1", md5="c9d0adcbe28cf54ef93dc50d8876ca88")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice@0.20:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
