# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultius(RPackage):
	"""Functions for the Courses Multivariate Analysis and Computer
Intensive Methods

	Provides utility functions for multivariate analysis (factor analysis, discriminant analysis, and others). The package is primary written for the course Multivariate analysis and for the course Computer intensive methods at the masters program of Applied Statistics at University of Ljubljana.
	"""
	
	cran = "multiUS" 

	version("1.2.3", md5="0c130d8c5c693fd1fb184330515667d3")

	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
