# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkgdepr(RPackage):
	"""Statically Determine Function Dependencies Between Packages

	Statically determine and visualize the function dependencies
    within and across packages. This may be useful for managing function 
    dependencies across a code base of multiple R packages.
	"""
	
	homepage = "https://pkgdepR.org/"
	cran = "pkgdepR" 

	version("1.0.0", md5="5fbd24721bbf8639cc7af09f98a18cc0")

	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
