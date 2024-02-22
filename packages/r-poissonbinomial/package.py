# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoissonbinomial(RPackage):
	"""Efficient Computation of Ordinary and Generalized Poisson
Binomial Distributions

	Efficient implementations of multiple exact and approximate methods as described in Hong (2013) <doi:10.1016/j.csda.2012.10.006>, Biscarri, Zhao & Brunner (2018) <doi:10.1016/j.csda.2018.01.007> and Zhang, Hong & Balakrishnan (2018) <doi:10.1080/00949655.2018.1440294> for computing the probability mass, cumulative distribution and quantile functions, as well as generating random numbers for both the ordinary and generalized Poisson binomial distribution.
	"""
	
	homepage = "https://github.com/fj86/PoissonBinomial"
	cran = "PoissonBinomial" 

	version("1.2.6", md5="c2853dab175d76163d1c8ceb0dd9b302")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("fftw@3.3:", type=("build", "link", "run"))
