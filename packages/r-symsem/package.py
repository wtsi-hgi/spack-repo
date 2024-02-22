# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSymsem(RPackage):
	"""Symbolic Computation for Structural Equation Models

	A collection of functions for symbolic computation using the
			 'caracas' package for structural equation models and other
			 statistical analyses. Among its features is the ability
			 to calculate the model-implied covariance (and correlation)
			 matrix and the sampling covariance matrix of variable functions
			 using the delta method.
	"""
	
	homepage = "https://github.com/mikewlcheung/symsem"
	cran = "symSEM" 

	version("0.2", md5="5f309676d1fe3bd2846f1805b4ce428a")

	depends_on("r-caracas", type=("build", "run"))
	depends_on("r-openmx", type=("build", "run"))
	depends_on("r-metasem", type=("build", "run"))
	depends_on("python", type=("build", "link", "run"))
