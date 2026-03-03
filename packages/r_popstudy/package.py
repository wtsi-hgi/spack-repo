# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopstudy(RPackage):
	"""Applied Techniques to Demographic and Time Series Analysis

	The use of overparameterization is proposed with combinatorial analysis to test a broader spectrum of possible ARIMA models.
    In the selection of ARIMA models, the most traditional methods such as correlograms or others, do not usually cover many alternatives to define the number of coefficients to be estimated in the model, which represents an estimation method that is not the best.
    The popstudy package contains several tools for statistical analysis in demography and time series based in Shryock research (Shryock et. al. (1980) <https://books.google.co.cr/books?id=8Oo6AQAAMAAJ>).
	"""
	
	homepage = "https://www.cesargamboasanabria.com"
	cran = "popstudy" 

	version("1.0.1", md5="32e61433fb7ecd2950770c006539daa7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-demography", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-rcompanion", type=("build", "run"))
	depends_on("r-corrr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-correlation", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rainbow", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
