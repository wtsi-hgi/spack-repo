# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyhugeplot(RPackage):
	"""Efficient Plotting of Large-Sized Data

	
    A tool to plot data with a large sample size using 'shiny' and 'plotly'.
    Relatively small samples are obtained from the original data using a specific algorithm.
    The samples are updated according to a user-defined x range.
    Jonas Van Der Donckt, Jeroen Van Der Donckt, Emiel Deprost (2022) <https://github.com/predict-idlab/plotly-resampler>.
	"""
	
	cran = "shinyHugePlot" 

	version("0.2.6", md5="ee74cb630fbb0d4109f6db4f9a8c015b")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-plotly@4.10:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.9:", type=("build", "run"))
	depends_on("r-tibble@3.1.7:", type=("build", "run"))
	depends_on("r-tidyr@1.2:", type=("build", "run"))
	depends_on("r-tidyselect@1.1.2:", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-nanotime@0.3.6:", type=("build", "run"))
	depends_on("r-assertthat@0.2.1:", type=("build", "run"))
	depends_on("r-bit64@4.0.5:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.8:", type=("build", "run"))
	depends_on("r-lazyeval@0.2.2:", type=("build", "run"))
	depends_on("r-shinyjs@2.1:", type=("build", "run"))
	depends_on("r-htmltools@0.5.2:", type=("build", "run"))
	depends_on("r-rlang@1.0.5:", type=("build", "run"))
