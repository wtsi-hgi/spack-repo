# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHettreatreg(RPackage):
	"""Heterogeneous Treatment Effects in Regression Analysis

	Computes diagnostics for linear regression when treatment effects are heterogeneous.
    The output of 'hettreatreg' represents ordinary least squares (OLS) 
    estimates of the effect of a binary treatment as a weighted average of the average treatment effect 
    on the treated (ATT) and the average treatment effect on the untreated (ATU). 
    The program estimates the OLS weights on these parameters, computes the associated model diagnostics, 
    and reports the implicit OLS estimate of the average treatment effect (ATE). 
    See Sloczynski (2019), <http://people.brandeis.edu/~tslocz/Sloczynski_paper_regression.pdf>.
	"""
	
	homepage = "https://github.com/tslocz/hettreatreg"
	cran = "hettreatreg" 

	version("0.1.0", md5="ec5a63731532e635ca8608005c68ad3f")

	depends_on("r@3.1:", type=("build", "run"))
