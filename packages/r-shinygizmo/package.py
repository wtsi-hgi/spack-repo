# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinygizmo(RPackage):
	"""Custom Components for Shiny Applications

	Provides useful UI components and input widgets for 'Shiny'
    applications.  The offered components allow to apply non-standard
    operations and view to your 'Shiny' application, but also help to
    overcome common performance issues.
	"""
	
	cran = "shinyGizmo" 

	version("0.4.2", md5="a41610e7f7ccf27a0275cd05dafd7fe4")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-shinywidgets@0.7:", type=("build", "run"))
