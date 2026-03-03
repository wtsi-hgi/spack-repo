# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROasisr(RPackage):
	"""Outright Tool for the Analysis of Spatial Inequalities and
Segregation

	A set of indexes and tests for the analysis of social segregation.
	"""
	
	cran = "OasisR" 

	version("3.1.0", md5="b82af51a2ced757de37ae10b6dc61f86")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-spdep@1.2.8:", type=("build", "run"))
	depends_on("r-measurements@1.5.1:", type=("build", "run"))
	depends_on("r-sf@1.0.14:", type=("build", "run"))
	depends_on("r-lwgeom@0.2.13:", type=("build", "run"))
	depends_on("r-seg@0.5.7:", type=("build", "run"))
	depends_on("r-outliers@0.15:", type=("build", "run"))
