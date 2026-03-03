# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydrotoolbox(RPackage):
	"""Hydrological Tools for Handling Hydro-Meteorological Data
Records

	Read, plot, manipulate and process hydro-meteorological data records (with special features for Argentina and Chile data-sets).
	"""
	
	homepage = "https://gitlab.com/ezetoum27/hydrotoolbox"
	cran = "hydrotoolbox" 

	version("1.1.2", md5="fc291340004abf7b340ee961e0d9d1a3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
