# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBalancecheck(RPackage):
	"""Balance Check for Multiple Covariates in Matched Observational
Studies

	Two practical tests are provided for assessing whether multiple covariates in a treatment group and a matched control group are balanced in observational studies. 
	"""
	
	cran = "BalanceCheck" 

	version("0.2", md5="b781524e0228f8a66090dce4050c1d75")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
