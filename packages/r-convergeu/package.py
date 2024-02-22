# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvergeu(RPackage):
	"""Monitoring Convergence of EU Countries

	Indicators and measures by country and time describe
    what happens at economic and social levels. This package provides
    functions to calculate several measures of convergence after imputing
    missing values. The automated downloading of Eurostat data,
    followed by the production of country fiches and indicator fiches,
    makes possible to produce automated reports.
    The Eurofound report (<doi:10.2806/68012>)
    "Upward convergence in the EU: Concepts, measurements and indicators", 
    2018, is a detailed  presentation of  convergence.
	"""
	
	homepage = "https://www.eurofound.europa.eu/system/files/2022-04/introduction-to-the-convergeu-package-0.6.4-tutorial-v2-apr2022.pdf"
	cran = "convergEU" 

	version("0.7.3.2", md5="869cabb5f40c135c5b562ed85bd18379")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-eurostat", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
