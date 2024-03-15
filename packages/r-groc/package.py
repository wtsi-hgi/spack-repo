# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGroc(RPackage):
	"""Generalized Regression on Orthogonal Components

	Robust multiple or multivariate linear regression, nonparametric regression on orthogonal components, classical or robust partial least squares models as described in Bilodeau, Lafaye De Micheaux and Mahdi (2015) <doi:10.18637/jss.v065.i01>.
	"""
	
	cran = "groc" 

	version("1.0.9", md5="889fc3948decf9287db02802066d21da")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
