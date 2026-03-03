# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCaic4(RPackage):
	"""Conditional Akaike Information Criterion for 'lme4' and 'nlme'

	Provides functions for the estimation of the conditional Akaike
    information in generalized mixed-effect models fitted with (g)lmer() 
    from 'lme4', lme() from 'nlme' and gamm() from 'mgcv'.
    For a manual on how to use 'cAIC4', see Saefken et al. (2021) <doi:10.18637/jss.v099.i08>.
	"""
	
	cran = "cAIC4" 

	version("1.0", md5="9ee994ed8d3249bd5df4d1a9d3b0c769", url="https://cran.r-project.org/src/contrib/cAIC4_1.0.tar.gz")

	depends_on("r-lme4@1.1.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rlrsim", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
