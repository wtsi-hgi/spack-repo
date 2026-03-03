# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROlympicrshiny(RPackage):
	"""'Shiny' Application for Olympic Data

	'Shiny' Application to visualize Olympic Data. From 1896 to
    2016. Even Winter Olympics events are included. Data is from Kaggle at
    <https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results>.
	"""
	
	homepage = "https://github.com/Amalan-ConStat/OlympicRshiny"
	cran = "OlympicRshiny" 

	version("1.0.1", md5="ffcbc53eed733bcebec1955719d25578")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-config@0.3.1:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-golem@0.3.5:", type=("build", "run"))
	depends_on("r-shiny@1.7.4:", type=("build", "run"))
	depends_on("r-shinybusy", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
	depends_on("r-summarytools", type=("build", "run"))
