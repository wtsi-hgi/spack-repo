# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKscorrect(RPackage):
	"""Lilliefors-Corrected Kolmogorov-Smirnov Goodness-of-Fit Tests

	Implements the Lilliefors-corrected Kolmogorov-Smirnov test for use
    in goodness-of-fit tests, suitable when population parameters are unknown and
    must be estimated by sample statistics. P-values are estimated by simulation.
    Can be used with a variety of continuous distributions, including normal,
    lognormal, univariate mixtures of normals, uniform, loguniform, exponential,
    gamma, and Weibull distributions. Functions to generate random numbers and
    calculate density, distribution, and quantile functions are provided for use
    with the log uniform and mixture distributions.
	"""
	
	homepage = "https://github.com/pnovack-gottshall/KScorrect"
	cran = "KScorrect" 

	version("1.4.0", md5="f23bc419fb8126600fb8f7f790f437bb")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r-doparallel@1.0.14:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-iterators@1.0.10:", type=("build", "run"))
	depends_on("r-mclust@5.4:", type=("build", "run"))
