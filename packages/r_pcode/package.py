# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcode(RPackage):
	"""Estimation of an Ordinary Differential Equation Model by
Parameter Cascade Method

	An implementation of the parameter cascade method in Ramsay, J. O., Hooker,G., Campbell, D., and Cao, J. (2007) for estimating ordinary differential equation models with missing or complete observations. It combines smoothing method and profile estimation to estimate any non-linear dynamic system. The package also offers variance estimates for parameters of interest based on either bootstrap or Delta method.  
	"""
	
	homepage = "https://github.com/alex-haixuw/PCODE"
	cran = "pCODE" 

	version("0.9.4", md5="631e05142ef670af9a71deaa504ea8c2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
