# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatstatGui(RPackage):
	"""Interactive Graphics Functions for the 'spatstat' Package

	Extension to the 'spatstat' package, containing
	     interactive graphics capabilities.
	"""
	
	cran = "spatstat.gui" 

	version("3.0-1", md5="bc5d1f5e57070382840792d009437bfd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-spatstat-geom@3:", type=("build", "run"))
	depends_on("r-spatstat-random@3.0.0:", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-spatstat-model@3:", type=("build", "run"))
	depends_on("r-spatstat-linnet@3:", type=("build", "run"))
	depends_on("r-spatstat-data@3:", type=("build", "run"))
	depends_on("r-spatstat@3:", type=("build", "run"))
	depends_on("r-rpanel", type=("build", "run"))
	depends_on("r-spatstat-utils@3:", type=("build", "run"))
