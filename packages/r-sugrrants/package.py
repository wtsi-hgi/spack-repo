# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSugrrants(RPackage):
	"""Supporting Graphs for Analysing Time Series

	Provides 'ggplot2' graphics for analysing time
    series data. It aims to fit into the 'tidyverse' and grammar of
    graphics framework for handling temporal data.
	"""
	
	homepage = "https://pkg.earo.me/sugrrants/"
	cran = "sugrrants" 

	version("0.2.8", md5="44371cf4239b152045877d572cea84c2")

	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-lubridate@1.7.1:", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
