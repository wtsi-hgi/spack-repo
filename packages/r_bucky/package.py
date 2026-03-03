# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBucky(RPackage):
	"""Bucky's Archive for Data Analysis in the Social Sciences

	Provides functions for various statistical techniques commonly used in the social sciences, including functions to compute clustered robust standard errors, combine results across multiply-imputed data sets, and simplify the addition of robust and clustered robust standard errors.
	"""
	
	homepage = "https://github.com/atahk/bucky"
	cran = "bucky" 

	version("1.0.7", md5="7f8d9dab538eecb09d8bcff41c62271e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
