# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDelaporte(RPackage):
	"""Statistical Functions for the Delaporte Distribution

	Provides probability mass, distribution, quantile, random-variate
    generation, and method-of-moments parameter-estimation functions for the
    Delaporte distribution with parameterization based on Vose (2008)
    <isbn:9780470512845>. The Delaporte is a discrete probability distribution
    which can be considered the convolution of a negative binomial distribution
    with a Poisson distribution. Alternatively, it can be considered a counting
    distribution with both Poisson and negative binomial components. It has been
    studied in actuarial science as a frequency distribution which has more
    variability than the Poisson, but less than the negative binomial.
	"""
	
	homepage = "https://github.com/aadler/Delaporte"
	cran = "Delaporte" 

	version("8.3.0", md5="cc965f62f3d69e9c785e98890c9536db")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("gcc", type=("build", "link", "run"))
