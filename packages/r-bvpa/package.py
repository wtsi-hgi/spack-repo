# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBvpa(RPackage):
	"""Bivariate Pareto Distribution

	Implements the EM algorithm with one-step Gradient Descent method to estimate
             the parameters of the Block-Basu bivariate Pareto distribution with location
             and scale. We also found parametric bootstrap and asymptotic confidence 
             intervals based on the observed Fisher information of scale and shape parameters,
             and exact confidence intervals for location parameters. Details are in 
             Biplab Paul and Arabin Kumar Dey (2023) <doi:10.48550/arXiv.1608.02199>
             "An EM algorithm for absolutely continuous Marshall-Olkin bivariate Pareto
             distribution with location and scale"; 
             E L Lehmann and George Casella (1998) <doi:10.1007/b98854> "Theory of Point Estimation";
             Bradley Efron and R J Tibshirani (1994) <doi:10.1201/9780429246593> 
             "An Introduction to the Bootstrap"; 
             A P Dempster, N M Laird and D B Rubin
             (1977) <www.jstor.org/stable/2984875> "Maximum Likelihood from Incomplete
             Data via the EM Algorithm".
	"""
	
	cran = "bvpa" 

	version("1.0.0", md5="0d9dc0f10631eef1908b8fe45dce9836")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
