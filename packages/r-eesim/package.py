# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REesim(RPackage):
	"""Simulate and Evaluate Time Series for Environmental Epidemiology

	Provides functions to create simulated time series of environmental
    exposures (e.g., temperature, air pollution) and health outcomes for use in
    power analysis and simulation studies in environmental epidemiology. This
    package also provides functions to evaluate the results of simulation studies
    based on these simulated time series. This work was supported by a grant
    from the National Institute of Environmental Health Sciences (R00ES022631) and
    a fellowship from the Colorado State University Programs for Research and
    Scholarly Excellence.
	"""
	
	homepage = "http://github.com/sakoehler7/eesim"
	cran = "eesim" 

	version("0.1.0", md5="9b8ed4b23ed10619e86aa71eadd5c865")

	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-lubridate@1.5.6:", type=("build", "run"))
	depends_on("r-purrr@0.2.2:", type=("build", "run"))
	depends_on("r-viridis@0.4:", type=("build", "run"))
