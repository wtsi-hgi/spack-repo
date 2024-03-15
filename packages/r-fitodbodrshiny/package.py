# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFitodbodrshiny(RPackage):
	"""'Shiny' Application for R Package 'fitODBOD'

	For binomial outcome data Alternate Binomial Distributions
    and Binomial Mixture Distributions are fitted when overdispersion is
    available.
	"""
	
	homepage = "https://github.com/Amalan-ConStat/fitODBODRshiny"
	cran = "fitODBODRshiny" 

	version("1.0.2", md5="b8ca868d8b44d8514ee8cdd53eba8656")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bslib", type=("build", "run"))
	depends_on("r-config@0.3.2:", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-golem@0.4.1:", type=("build", "run"))
	depends_on("r-shiny@1.8:", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-shinyscreenshot", type=("build", "run"))
