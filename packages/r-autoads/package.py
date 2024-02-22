# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoads(RPackage):
	"""Advertisement Metrics Calculation

	Calculations of the most common metrics of automated advertisement and plotting of them with trend and forecast. Calculations and description of metrics is taken from different RTB platforms support documentation. Plotting and forecasting is based on packages 'forecast', described in Rob J Hyndman and George Athanasopoulos (2021) "Forecasting: Principles and Practice" <https://otexts.com/fpp3/> and Rob J Hyndman et al "Documentation for 'forecast'" (2003) <https://pkg.robjhyndman.com/forecast/>, and 'ggplot2', described in Hadley Wickham et al "Documentation for 'ggplot2'" (2015) <https://ggplot2.tidyverse.org/>, and Hadley Wickham, Danielle Navarro, and Thomas Lin Pedersen (2015) "ggplot2: Elegant Graphics for Data Analysis" <https://ggplot2-book.org/>.
	"""
	
	cran = "AutoAds" 

	version("0.1.0", md5="fec12cbec66f9a7bff270bee4aa01ffc")

	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
