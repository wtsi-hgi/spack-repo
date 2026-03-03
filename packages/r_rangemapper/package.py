# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRangemapper(RPackage):
	"""A Platform for the Study of Macro-Ecology of Life History Traits

	Tools for generation of (life-history) traits and diversity maps on hexagonal or square grids. Valcu et al.(2012) <doi:10.1111/j.1466-8238.2011.00739.x>.
	"""
	
	homepage = "https://github.com/mpio-be/rangeMapper"
	cran = "rangeMapper" 

	version("2.0.3", md5="95a6c17d5b3e80cb2c712f7ad4aa2817")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-exactextractr", type=("build", "run"))
