# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtdist(RPackage):
	"""Extending the Range of Functions for Probability Distributions

	A consistent, unified and extensible
    framework for estimation of parameters for probability distributions, including 
    parameter estimation procedures that allow for weighted samples; the current set of distributions included are: the standard beta, The four-parameter beta, Burr, gamma, Gumbel, Johnson SB and SU, Laplace, logistic, normal, symmetric truncated normal, truncated normal, symmetric-reflected truncated beta, standard symmetric-reflected truncated beta, triangular, uniform, and Weibull distributions; decision criteria and selections based on these decision criteria.
	"""
	
	cran = "ExtDist" 

	version("0.7-2", md5="e665a92eae5e0e9b5b120b527d3ca7ff")

	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
