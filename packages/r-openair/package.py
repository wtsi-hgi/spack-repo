# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenair(RPackage):
	"""Tools for the Analysis of Air Pollution Data

	Tools to analyse, interpret and understand air pollution
    data. Data are typically regular time series and air quality
    measurement, meteorological data and dispersion model output can be
    analysed. The package is described in Carslaw and Ropkins (2012,
    <doi:10.1016/j.envsoft.2011.09.008>) and subsequent papers.
	"""
	
	homepage = "https://davidcarslaw.github.io/openair/"
	cran = "openair" 

	version("2.18-0", md5="301c3df8314138c6193499cff523c396")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
