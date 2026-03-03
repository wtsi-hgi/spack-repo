# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrexamples(RPackage):
	"""Collection of Practical Institutional Research Examples and
Tutorials

	Provides examples of code for analyzing data or accomplishing tasks that may be useful to institutional or educational researchers.
	"""
	
	homepage = "https://github.com/vinhdizzo/IRexamples"
	cran = "IRexamples" 

	version("0.0.4", md5="a91005953ef64adfb2eb5ff151ea2ade")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-twang", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-rstanarm", type=("build", "run"))
	depends_on("r-rselenium", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-disimpact", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-tidygeocoder", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-geodist", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-tigris", type=("build", "run"))
	depends_on("r-tidycensus", type=("build", "run"))
