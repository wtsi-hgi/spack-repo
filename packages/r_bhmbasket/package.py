# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBhmbasket(RPackage):
	"""Bayesian Hierarchical Models for Basket Trials

	Provides functions for the evaluation of basket
    trial designs with binary endpoints. Operating characteristics of a
    basket trial design are assessed by simulating trial data according to
    scenarios, analyzing the data with Bayesian hierarchical models (BHMs), and
    assessing decision probabilities on stratum and trial-level based on Go / No-go decision making.
    The package is build for high flexibility regarding decision rules,
    number of interim analyses, number of strata, and recruitment.
    The BHMs proposed by
    Berry et al. (2013) <doi:10.1177/1740774513497539>
    and Neuenschwander et al. (2016) <doi:10.1002/pst.1730>,
    as well as a model that combines both approaches are implemented.
    Functions are provided to implement Bayesian decision rules as for example
    proposed by Fisch et al. (2015) <doi:10.1177/2168479014533970>.
    In addition, posterior point estimates (mean/median) and credible intervals
    for response rates and some model parameters can be calculated.
    For simulated trial data, bias and mean squared errors of posterior
    point estimates for response rates can be provided.
	"""
	
	homepage = "https://CRAN.R-project.org/package=bhmbasket"
	cran = "bhmbasket" 

	version("0.9.5", md5="168c3c8e312b45e95a1ab7b2a462d011")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-r2jags@0.7.1:", type=("build", "run"))
	depends_on("jags@4.0.0:4.999.999", type=("build", "link", "run"))
