# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbmedian(RPackage):
	"""Scalable Bayes with Median of Subset Posteriors

	Median-of-means is a generic yet powerful framework for scalable and robust estimation. A framework for Bayesian analysis is called M-posterior, which estimates a median of subset posterior measures. For general exposition to the topic, see the paper by Minsker (2015) <doi:10.3150/14-BEJ645>.
	"""
	
	cran = "SBmedian" 

	version("0.1.1", md5="2c398909edc13cae15e472e7389e539a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
