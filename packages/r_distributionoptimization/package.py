# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistributionoptimization(RPackage):
	"""Distribution Optimization

	Fits Gaussian Mixtures by applying evolution. As fitness function a mixture of the chi square test for distributions and a novel measure for approximating the common area under curves between multiple Gaussians is used. The package presents an alternative to the commonly used Likelihood Maximization as is used in Expectation Maximization. The algorithm and applications of this package are published under: Lerch, F., Ultsch, A., Lotsch, J. (2020) <doi:10.1038/s41598-020-57432-w>. The evolution is based on the 'GA' package: Scrucca, L. (2013) <doi:10.18637/jss.v053.i04> while the Gaussian Mixture Logic stems from 'AdaptGauss': Ultsch, A, et al. (2015) <doi:10.3390/ijms161025897>. 
	"""
	
	cran = "DistributionOptimization" 

	version("1.2.6", md5="60c6076b8ab5428b2b5236458396df98")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ga", type=("build", "run"))
	depends_on("r-adaptgauss", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
