# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyusda(RPackage):
	"""A Minimal Tool Set for Gathering USDA Quick Stat Data for
Analysis and Visualization

	Provides a consistent API to pull United States Department of
    Agriculture census and survey data from the National Agricultural
    Statistics Service (NASS) QuickStats service.
	"""
	
	homepage = "https://bradlindblad.github.io/tidyUSDA/"
	cran = "tidyUSDA" 

	version("0.4.1", md5="c62cb15c114123b90d0ab9a5db4089b7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fuzzyjoin@0.1.6:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tigris@1:", type=("build", "run"))
