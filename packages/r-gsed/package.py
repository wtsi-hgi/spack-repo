# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsed(RPackage):
	"""Group Sequential Enrichment Design

	Provides function to apply "Group sequential enrichment design incorporating subgroup selection" (GSED) method proposed by Magnusson and Turnbull (2013) <doi:10.1002/sim.5738>.
	"""
	
	cran = "GSED" 

	version("2.6", md5="f5dcf9b29fba8a128db742dce85cae6b")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-memoise@1:", type=("build", "run"))
	depends_on("r-rootsolve@1.6.6:", type=("build", "run"))
	depends_on("r-survival@2.37.7:", type=("build", "run"))
	depends_on("r-r-utils@2.3:", type=("build", "run"))
