# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnlc(RPackage):
	"""Differential Network Local Consistency Analysis

	Using Local Moran's I for detection of differential network local consistency.
	"""
	
	cran = "DNLC" 

	version("1.0.0", md5="9f2712462ccf69f119e28f0dc36439c7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-gostats", type=("build", "run"))
	depends_on("r-locfdr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
