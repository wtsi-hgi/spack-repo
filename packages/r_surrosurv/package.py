# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurrosurv(RPackage):
	"""Evaluation of Failure Time Surrogate Endpoints in Individual
Patient Data Meta-Analyses

	Provides functions for the evaluation of
    surrogate endpoints when both the surrogate and the true endpoint are failure
    time variables. The approaches implemented are:
    (1) the two-step approach (Burzykowski et al, 2001) <DOI:10.1111/1467-9876.00244> with a copula model (Clayton, Plackett, Hougaard) at
    the first step and either a linear regression of log-hazard ratios at the second
    step (either adjusted or not for measurement error);
    (2) mixed proportional hazard models estimated via mixed Poisson GLM
    (Rotolo et al, 2017 <DOI:10.1177/0962280217718582>).
	"""
	
	homepage = "https://github.com/Oncostat/surrosurv"
	cran = "surrosurv" 

	version("1.1.26", md5="22f2b2c9868a8e6555b2938ef17cf69b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-eha", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-mvmeta", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-parfm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
