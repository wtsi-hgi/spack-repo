# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetourr(RPackage):
	"""Portable and Performant Tour Animations

	Provides 2D and 3D tour animations as HTML widgets. The user can interact with the widgets using orbit controls, tooltips, brushing, and timeline controls. Linked brushing is supported using 'crosstalk', and widgets can be embedded in Shiny apps or HTML documents. 
	"""
	
	homepage = "https://casperhart.github.io/detourr/"
	cran = "detourr" 

	version("0.1.0", md5="5f16ffd62d8e84bf82d9d4620d158ecf")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-tourr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
