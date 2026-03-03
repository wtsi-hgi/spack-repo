# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpsmooth(RPackage):
	"""LP Smoothed Inference and Graphics

	Classical tests of goodness-of-fit aim to validate the conformity of a postulated model to the data under study. In their standard formulation, however, they do not allow exploring how the hypothesized model deviates from the truth nor do they provide any insight into how the rejected model could be improved to better fit the data. To overcome these shortcomings, we establish a comprehensive framework for goodness-of-fit which naturally integrates modeling, estimation, inference and graphics. In this package, the deviance tests and comparison density plots are performed to conduct the LP smoothed inference, where the letter L denotes nonparametric methods based on quantiles and P stands for polynomials. Simulations methods are used to perform variance estimation, inference and post-selection adjustments. Algeri S. and Zhang X. (2020) <arXiv:2005.13011>.
	"""
	
	cran = "LPsmooth" 

	version("0.1.3", md5="460024955e3306b047f2d5caef3693b3")

	depends_on("r-lpgraph", type=("build", "run"))
	depends_on("r-lpbkg", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-polynom", type=("build", "run"))
