# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RBlme(RPackage):
	"""Bayesian Linear Mixed-Effects Models

	Maximum a posteriori estimation for linear and generalized linear mixed-effects models in a Bayesian setting, implementing the methods of Chung, et al. (2013) <doi:10.1007/s11336-013-9328-2>. Extends package 'lme4' (Bates, Maechler, Bolker, and Walker (2015) <doi:10.18637/jss.v067.i01>).
	"""
	
	homepage = "https://github.com/vdorie/blme"
	cran = "blme" 

	version("1.0-5", md5="7a3b04b9cf6a638139827031647710ff")

	depends_on("r@3.0-0:", type=("build", "run"))
	depends_on("r-lme4@1.0-6:", type=("build", "run"))
