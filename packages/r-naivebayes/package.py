# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNaivebayes(RPackage):
	"""High Performance Implementation of the Naive Bayes Algorithm

	In this implementation of the Naive Bayes classifier following class conditional distributions are available: Bernoulli, Categorical, Gaussian, Poisson and non-parametric representation of the class conditional density estimated via Kernel Density Estimation. Implemented classifiers handle missing data and can take advantage of sparse data.
	"""
	
	homepage = "https://github.com/majkamichal/naivebayes"
	cran = "naivebayes" 

	version("0.9.7", md5="7f3467dcef693166e74c96ecd1b85d46")

