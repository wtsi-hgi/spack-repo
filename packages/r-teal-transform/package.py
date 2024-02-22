# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTealTransform(RPackage):
	"""Functions for Extracting and Merging Data in the 'teal'
Framework

	A standardized user interface for column selection, that
    facilitates dataset merging in 'teal' framework.
	"""
	
	homepage = "https://insightsengineering.github.io/teal.transform/"
	cran = "teal.transform" 

	version("0.5.0", md5="e1676185b225f09165435e9addbe49b4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate@2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-lifecycle@0.2:", type=("build", "run"))
	depends_on("r-logger@0.2:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-shiny@1.6:", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinyvalidate", type=("build", "run"))
	depends_on("r-teal-data@0.5:", type=("build", "run"))
	depends_on("r-teal-logger@0.1.1:", type=("build", "run"))
	depends_on("r-teal-widgets@0.4:", type=("build", "run"))
	depends_on("r-tidyr@0.8.3:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
