# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopulagamm(RPackage):
	"""Copula-Based Mixed Regression Models

	Estimation of 2-level factor copula-based regression models  for clustered data where the response variable can be either discrete or continuous. 
	"""
	
	cran = "CopulaGAMM" 

	version("0.4.1", md5="239a1e29b9a489556ff9f66808b7e17c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
