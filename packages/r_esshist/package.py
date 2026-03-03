# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsshist(RPackage):
	"""The Essential Histogram

	Provide an optimal histogram, in the sense of probability density estimation and features detection, by means of multiscale variational inference. In other words, the resulting histogram servers as an optimal density estimator, and meanwhile recovers the features, such as increases or modes, with both false positive and false negative controls. Moreover, it provides a parsimonious representation in terms of the number of blocks, which simplifies data interpretation. The only assumption for the method is that data points are independent and identically distributed, so it applies to fairly general situations, including continuous distributions, discrete distributions, and mixtures of both. For details see Li, Munk, Sieling and Walther (2016) <arXiv:1612.07216>. 
	"""
	
	cran = "essHist" 

	version("1.2.2", md5="791d4164458922b6e2c67e5ee122d8fc")

	depends_on("r@2.15.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
