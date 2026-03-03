# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHypothesis(RPackage):
	"""Wrapper for 'hypothes.is'

	Add, share and manage annotations for 'Shiny' applications and R Markdown documents via 'hypothes.is'.
	"""
	
	cran = "hypothesis" 

	version("1.1.0", md5="f831a55dbed4656ff64f46c7c784e19a")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
