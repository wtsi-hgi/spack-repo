# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrf(RPackage):
	"""Ordered Random Forests

	An implementation of the Ordered Forest estimator as developed 
    in Lechner & Okasa (2019) <arXiv:1907.02436>. The Ordered Forest flexibly
    estimates the conditional probabilities of models with ordered categorical
    outcomes (so-called ordered choice models). Additionally to common machine 
    learning algorithms the 'orf' package provides functions for estimating
    marginal effects as well as statistical inference thereof and thus provides
    similar output as in standard econometric models for ordered choice. The
    core forest algorithm relies on the fast C++ forest implementation from
    the 'ranger' package (Wright & Ziegler, 2017) <arXiv:1508.04409>.
	"""
	
	homepage = "https://github.com/okasag/orf"
	cran = "orf" 

	version("0.1.4", md5="abcd49b6a2147fddf5e32a611e4fff7c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
