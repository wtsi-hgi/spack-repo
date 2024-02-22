# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPersonalr(RPackage):
	"""Automated Personal Package Setup

	Functions to setup a personal R package that attaches given
    libraries and exports personal helper functions.
	"""
	
	homepage = "https://mrcaseb.github.io/personalr/index.html"
	cran = "personalr" 

	version("1.0.3", md5="dd0e360ac30c1d56fd23438c56ee761e")

	depends_on("r-desc", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rprojroot", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-xfun", type=("build", "run"))
