# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcexttools(RPackage):
	"""Analytical Procedures in Support of Brazilian Public Sector
External Auditing

	Set of analytical procedures based on advanced data analysis in support of Brazil's public sector external control activity.
	"""
	
	homepage = "http://github.com/brunomssmelo/RcextTools/"
	cran = "RcextTools" 

	version("0.1.1", md5="402be12800a945cacace0416232779f4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
