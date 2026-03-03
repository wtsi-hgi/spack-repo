# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovafillr(RPackage):
	"""Local Polynomial Regression of State Dependent Covariates in
State-Space Models

	Facilitates local polynomial regression for state dependent covariates in state-space models. The functionality can also be used from 'C++' based model builder tools such as 'Rcpp'/'inline', 'TMB', or 'JAGS'.
	"""
	
	homepage = "https://github.com/calbertsen/covafillr"
	cran = "covafillr" 

	version("0.4.4", md5="1159188d64b18a9e37fdfe56a1deaa04")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp@0.11:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
