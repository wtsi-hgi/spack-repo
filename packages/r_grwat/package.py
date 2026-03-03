# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrwat(RPackage):
	"""River Hydrograph Separation and Analysis

	River hydrograph separation and daily runoff time series analysis. Provides
  various filters to separate baseflow and quickflow. Implements advanced separation 
  technique by Rets et al. (2022) <doi:10.1134/S0097807822010146> which involves 
  meteorological data to reveal genetic components of the runoff: ground, rain, thaw 
  and spring (seasonal thaw). High-performance C++17 computation, annually aggregated 
  variables, statistical testing and numerous plotting functions for high-quality 
  visualization.
	"""
	
	homepage = "https://github.com/tsamsonov/grwat"
	cran = "grwat" 

	version("0.0.4", md5="07828f07f1c3d01989222a7de4c513e6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-trend", type=("build", "run"))
	depends_on("r-mblm", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
