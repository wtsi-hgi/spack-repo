# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpiflows(RPackage):
	"""Predicting Disease Spread from Flow Data

	Provides functions and classes designed to handle and visualise
    epidemiological flows between locations. Also contains a statistical method
    for predicting disease spread from flow data initially described in
    Dorigatti et al. (2017) <doi:10.2807/1560-7917.ES.2017.22.28.30572>.
    This package is part of the RECON (<https://www.repidemicsconsortium.org/>)
    toolkit for outbreak analysis.
	"""
	
	homepage = "https://www.repidemicsconsortium.org/epiflows/"
	cran = "epiflows" 

	version("0.2.1", md5="33768b820b17c34097e332bcdefc0e78")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-epicontacts", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-ggmap", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
