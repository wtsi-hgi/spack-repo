# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REfreadr(RPackage):
	"""Read European Eddy Fluxes CSV Files

	The European Eddy Fluxes Database Cluster distributes fluxes of different Green House Gases measured mainly using the eddy covariance technique acquired in sites involved in EU projects but also single sites in Europe, Africa and others continents that decided to share their measurements in the database <http://gaia.agraria.unitus.it>. The package provides two functions to load and row-wise bind CSV files distributed by the database. Currently only L2, L3, and L4 (L=Level), half-hourly and daily (aggregation) files are supported.
	"""
	
	cran = "efreadr" 

	version("0.2.2", md5="3a2436cf3938402a4904e372060cccd0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ensurer", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
