# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifer(RPackage):
	"""Identify Sites for Your Bird List

	A suite of tools to use the 'eBird' database 
    (<https://ebird.org/home/>) and APIs to compare users' species lists to 
    recent observations and create a report of the top sites to visit to see 
    new species.
	"""
	
	homepage = "https://jcoliver.github.io/lifeR/"
	cran = "lifeR" 

	version("1.0.1", md5="37ac90a34c2e907ca146481995a4a173")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-curl@4.3:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-knitr@1.31:", type=("build", "run"))
	depends_on("r-readr@1.4:", type=("build", "run"))
	depends_on("r-rmarkdown@2.7:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4.4:", type=("build", "run"))
	depends_on("r-maptiles@0.6.1:", type=("build", "run"))
	depends_on("r-terra@1.7.55:", type=("build", "run"))
	depends_on("r-tidyterra@0.5:", type=("build", "run"))
