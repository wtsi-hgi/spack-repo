# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComorosmaps(RPackage):
	"""Comoro Islands Maps

	Maps of Comoro Islands. Layers include the country coastline, each island coastline and administrative regions boundaries.
	"""
	
	homepage = "https://github.com/hhousni/comorosmaps"
	cran = "comorosmaps" 

	version("1.0.0", md5="287e695cc796ec6b9f3f0d86dcba0558")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
