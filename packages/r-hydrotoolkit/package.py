# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHydrotoolkit(RPackage):
	"""Hydrological Tools for Handling Hydro-Meteorological Data from
Argentina and Chile

	Read, plot, manipulate and process hydro-meteorological data from Argentina and Chile.
	"""
	
	cran = "hydroToolkit" 

	version("0.1.0", md5="9c94d6eb5131987555da0774194a525b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
