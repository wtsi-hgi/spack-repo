# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobflreg(RPackage):
	"""Robust Functional Linear Regression

	Functions for implementing robust methods for functional linear regression. In the functional linear regression, we consider scalar-on-function linear regression and function-on-function linear regression. More details, see Beyaztas, U., and Shang, H. L. (2021) <arXiv:2111.01238> and Beyaztas, U., and Shang, H. L. (2022) <arXiv:2203.05065>.
	"""
	
	cran = "robflreg" 

	version("1.2", md5="ff661e52a98f83c22bb33496b6157a12")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r-goffda", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
