# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidytable(RPackage):
	"""Tidy Interface to 'data.table'

	A tidy interface to 'data.table',
  giving users the speed of 'data.table' while using tidyverse-like syntax.
	"""
	
	homepage = "https://markfairbanks.github.io/tidytable/"
	cran = "tidytable" 

	version("0.11.0", md5="4ed032452640aa4847b8105333fa72b5")

	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-glue@1.4:", type=("build", "run"))
	depends_on("r-lifecycle@1.0.3:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
	depends_on("r-pillar@1.8:", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-vctrs@0.6:", type=("build", "run"))
