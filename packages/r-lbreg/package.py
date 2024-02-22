# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLbreg(RPackage):
	"""Log-Binomial Regression with Constrained Optimization

	Maximum likelihood estimation of log-binomial regression with special functionality when the MLE is on the boundary of the parameter space.
	"""
	
	cran = "lbreg" 

	version("1.3", md5="4d2404736e02c1219733520b5350e435")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
