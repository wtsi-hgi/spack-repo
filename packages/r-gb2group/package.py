# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGb2group(RPackage):
	"""Estimation of the Generalised Beta Distribution of the Second
Kind from Grouped Data

	Estimation of the generalized beta distribution of the second 
    kind (GB2) and related models using grouped data in form of income shares. 
    The GB2 family is a general class of distributions that provides an accurate 
    fit to income data. 'GB2group' includes functions to estimate the GB2, the 
    Singh-Maddala, the Dagum, the Beta 2, the Lognormal and the Fisk distributions. 
    'GB2group' deploys two different econometric strategies to estimate these 
    parametric distributions, the equally weighted minimum distance (EWMD) estimator and the  
    optimally weighted minimum distance (OMD) estimator. Asymptotic standard errors are reported for the 
    OMD estimates. Standard errors of the EWMD estimates are obtained by Monte 
    Carlo simulation. See Jorda et al. (2018) <arXiv:1808.09831> for a detailed 
    description of the estimation procedure. 
	"""
	
	cran = "GB2group" 

	version("0.3.0", md5="ca4f7941528220db03a9daaf7d757ad2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-gb2", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
