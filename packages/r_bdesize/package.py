# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdesize(RPackage):
	"""Efficient Determination of Sample Size in Balanced Design of
Experiments

	For a balanced design of experiments, this package calculates the sample size required to detect a certain standardized effect size, under a significance level. This package also provides three graphs; detectable standardized effect size vs power, sample size vs detectable standardized effect size, and sample size vs power, which show the mutual relationship between the sample size, power and the detectable standardized effect size. The detailed procedure is described in R. V. Lenth (2006-9) <https://homepage.divms.uiowa.edu/~rlenth/Power/>, Y. B. Lim (1998), M. A. Kastenbaum, D. G. Hoel and K. O. Bowman (1970) <doi:10.2307/2334851>, and Douglas C. Montgomery (2013, ISBN: 0849323312).
	"""
	
	cran = "BDEsize" 

	version("1.6", md5="b2ef78d07048f472f4d1be33f7fb1ae6")

	depends_on("r-fpow", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
