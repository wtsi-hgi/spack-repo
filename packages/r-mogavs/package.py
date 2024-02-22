# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMogavs(RPackage):
	"""Multiobjective Genetic Algorithm for Variable Selection in
Regression

	Functions for exploring the best subsets in regression with a genetic algorithm. The package is much faster than methods relying on complete enumeration, and is suitable for data sets with large number of variables. For more information, see Sinha, Malo & Kuosmanen (2015) <doi:10.1080/10618600.2014.899236>.
	"""
	
	cran = "mogavs" 

	version("1.1.0", md5="1dcb0329ad91b6c97cf3fe4d2a3b5437")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cvtools", type=("build", "run"))
