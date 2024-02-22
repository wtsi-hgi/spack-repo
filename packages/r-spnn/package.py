# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpnn(RPackage):
	"""Scale Invariant Probabilistic Neural Networks

	Scale invariant version of the original PNN proposed by Specht (1990) <doi:10.1016/0893-6080(90)90049-q> with the added functionality of allowing for smoothing along multiple dimensions while accounting for covariances within the data set. It is written in the R statistical programming language. Given a data set with categorical variables, we use this algorithm to estimate the probabilities of a new observation vector belonging to a specific category. This type of neural network provides the benefits of fast training time relative to backpropagation and statistical generalization with only a small set of known observations.
	"""
	
	cran = "spnn" 

	version("1.2.1", md5="c5e817a3870bc7c32505df6318f8a9d4")

	depends_on("r-mass@3.1.20:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
