# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSemiparDepcens(RPackage):
	"""Copula Based Cox Proportional Hazards Models for Dependent
Censoring

	Copula based Cox proportional hazards models for survival data subject to dependent 
    censoring. This approach does not assume that the parameter defining the copula is known. The 
    dependency parameter is estimated with other finite model parameters by maximizing a Pseudo 
    likelihood function. The cumulative hazard function is estimated via estimating equations 
    derived based on martingale ideas. Available copula functions include Frank, Gumbel and Normal
    copulas. Only Weibull and lognormal models are allowed for the censoring model, even though any
    parametric model that satisfies certain identifiability conditions could be used. Implemented 
    methods are described in the article "Copula based Cox proportional hazards models for dependent
    censoring" by Deresa and Van Keilegom (2023) <doi:10.1080/01621459.2022.2161387>. 
	"""
	
	homepage = "https://github.com/Nago2020/SemiPar.depCens"
	cran = "SemiPar.depCens" 

	version("0.1.1", md5="4be2c0ea0be975f5e4a11a8bc0cde32f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
