# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisit(RPackage):
	"""Vaccine Phase I Design with Simultaneous Evaluation of
Immunogenicity and Toxicity

	
    Phase I clinical trials are the first step in drug development to test
    a new drug or drug combination on humans. Typical designs of Phase I 
    trials use toxicity as the primary endpoint and aim to find the maximum 
    tolerable dosage. However, these designs are poorly applicable for the 
    development of cancer therapeutic vaccines because the expected safety 
    concerns for these vaccines are not as much as cytotoxic agents. The 
    primary objectives of a cancer therapeutic vaccine phase I trial thus 
    often include determining whether the vaccine shows biologic activity 
    and the minimum dose necessary to achieve a full immune or even clinical 
    response. This package implements a Bayesian Phase I cancer vaccine
    trial design that allows simultaneous evaluation of safety and
    immunogenicity outcomes. See Wang et al. (2019) <DOI:10.1002/sim.8021>
    for further details.
	"""
	
	cran = "visit" 

	version("2.2", md5="dc50b6756506d47c2914328f1dbf631c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rstan@2.14:", type=("build", "run"))
	depends_on("r-rcpp@1.0.2:", type=("build", "run"))
	depends_on("r-sqldf@0.4:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.2:", type=("build", "run"))
	depends_on("r-bh@1.69.0.1:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.5:", type=("build", "run"))
	depends_on("r-stanheaders@2.18.1.10:", type=("build", "run"))
