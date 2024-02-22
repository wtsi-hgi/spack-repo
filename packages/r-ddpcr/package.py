# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDdpcr(RPackage):
	"""Analysis and Visualization of Droplet Digital PCR in R and on
the Web

	An interface to explore, analyze, and visualize droplet digital PCR
    (ddPCR) data in R. This is the first non-proprietary software for analyzing
    two-channel ddPCR data. An interactive tool was also created and is available
    online to facilitate this analysis for anyone who is not comfortable with
    using R.
	"""
	
	homepage = "https://github.com/daattali/ddpcr"
	cran = "ddpcr" 

	version("1.15.2", md5="ee54a8ef3182ba3993c3ea3386fb26fd")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-dt@0.2:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-lazyeval@0.1.10:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-mixtools@1.0.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.1:", type=("build", "run"))
	depends_on("r-readr@0.1:", type=("build", "run"))
	depends_on("r-shiny@0.11:", type=("build", "run"))
	depends_on("r-shinydisconnect", type=("build", "run"))
	depends_on("r-shinyjs@0.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
