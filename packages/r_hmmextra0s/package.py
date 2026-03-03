# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmmextra0s(RPackage):
	"""Hidden Markov Models with Extra Zeros

	Contains functions for hidden Markov models with observations having extra zeros as defined in the following two publications, Wang, T., Zhuang, J., Obara, K. and Tsuruoka, H. (2016) <doi:10.1111/rssc.12194>; Wang, T., Zhuang, J., Buckby, J., Obara, K. and Tsuruoka, H. (2018) <doi:10.1029/2017JB015360>. The observed response variable is either univariate or bivariate Gaussian conditioning on presence of events, and extra zeros mean that the response variable takes on the value zero if nothing is happening. Hence the response is modelled as a mixture distribution of a Bernoulli variable and a continuous variable. That is, if the Bernoulli variable takes on the value 1, then the response variable is Gaussian, and if the Bernoulli variable takes on the value 0, then the response is zero too. This package includes functions for simulation, parameter estimation, goodness-of-fit, the Viterbi algorithm, and plotting the classified 2-D data. Some of the functions in the package are based on those of the R package 'HiddenMarkov' by David Harte. This updated version has included an example dataset and R code examples to show how to transform the data into the objects needed in the main functions. We have also made changes to increase the speed of some of the functions.
	"""
	
	homepage = "https://www.stats.otago.ac.nz/?people=ting_wang"
	cran = "HMMextra0s" 

	version("1.1.0", md5="2c146e3337b0cd9a864baa33db11c58b")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
