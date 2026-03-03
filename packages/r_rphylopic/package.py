# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRphylopic(RPackage):
	"""Get Silhouettes of Organisms from PhyloPic

	Work with the PhyloPic Web Service (<http://api-docs.phylopic.org/v2/>) 
    to fetch silhouette images of organisms. Includes functions for adding 
    silhouettes to both base R plots and ggplot2 plots.
	"""
	
	homepage = "https://rphylopic.palaeoverse.org"
	cran = "rphylopic" 

	version("1.3.0", md5="2a466740bb10033f8f75efdf7bdc3df4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-grimport2@0.3:", type=("build", "run"))
	depends_on("r-rsvg@2.6:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
