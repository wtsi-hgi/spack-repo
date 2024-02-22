# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatstatLocal(RPackage):
	"""Extension to 'spatstat' for Local Composite Likelihood

	Extension to the 'spatstat' package, enabling the user
	     to fit point process models to point pattern data
	     by local composite likelihood ('geographically weighted
	     regression').
	"""
	
	cran = "spatstat.local" 

	version("5.0-1", md5="26415ac404d7b6dd9989ffb1a7496e1b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat-data@3:", type=("build", "run"))
	depends_on("r-spatstat-sparse@3:", type=("build", "run"))
	depends_on("r-spatstat-geom@3:", type=("build", "run"))
	depends_on("r-spatstat-random@3:", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-model@3:", type=("build", "run"))
	depends_on("r-spatstat@3:", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-spatstat-utils@3:", type=("build", "run"))
