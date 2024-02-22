# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgeva(RPackage):
	"""Binary Generalized Extreme Value Additive Models

	Routine for fitting regression models for binary rare events with linear and nonlinear covariate effects when using the quantile function of the Generalized Extreme Value random variable.
	"""
	
	homepage = "http://www.ucl.ac.uk/statistics/people/giampieromarra"
	cran = "bgeva" 

	version("0.3-1", md5="c4d1b46125d4d283249c41352242c41c")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
