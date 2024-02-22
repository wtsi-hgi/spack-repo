# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCransearcher(RPackage):
	"""RStudio Addin for Searching Packages in CRAN Database Based on
Keywords

	One of the strengths of R is its vast package ecosystem. Indeed, R packages extend from visualization to Bayesian inference and from spatial analyses to pharmacokinetics (<https://cran.r-project.org/web/views/>). There is probably not an area of quantitative research that isn't represented by at least one R package. At the time of this writing, there are more than 10,000 active CRAN packages. Because of this massive ecosystem, it is important to have tools to search and learn about packages related to your personal R needs. For this reason, we developed an RStudio addin capable of searching available CRAN packages directly within RStudio.
	"""
	
	homepage = "https://github.com/RhoInc/CRANsearcher"
	cran = "CRANsearcher" 

	version("1.0.0", md5="287cf65d3c5cc0161bf54de66a0f53de")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
