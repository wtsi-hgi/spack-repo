# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRainette(RPackage):
	"""The Reinert Method for Textual Data Clustering

	An R implementation of the Reinert text clustering method. For more 
    details about the algorithm see the included vignettes or Reinert (1990) 
    <doi:10.1177/075910639002600103>.
	"""
	
	homepage = "https://juba.github.io/rainette/"
	cran = "rainette" 

	version("0.3.1.1", md5="7858a1d44a605634edae141752e47c76")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-quanteda@2.1:", type=("build", "run"))
	depends_on("r-quanteda-textstats", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-dendextend", type=("build", "run"))
	depends_on("r-ggwordcloud", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-highr", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
