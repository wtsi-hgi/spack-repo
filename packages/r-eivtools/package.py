# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REivtools(RPackage):
	"""Measurement Error Modeling Tools

	This includes functions for analysis with error-prone covariates, including deconvolution, latent regression and errors-in-variables regression.  It implements methods by Rabe-Hesketh et al. (2003) <doi:10.1191/1471082x03st056oa>, Lockwood and McCaffrey (2014) <doi:10.3102/1076998613509405>, and Lockwood and McCaffrey (2017) <doi:10.1007/s11336-017-9556-y>, among others.
	"""
	
	cran = "eivtools" 

	version("0.1-8", md5="fdd14b96fddfc2ae2d6fb9fa9b526191")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-r2jags", type=("build", "run"))
