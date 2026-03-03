# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrazilmet(RPackage):
	"""Download and Processing of Automatic Weather Stations (AWS) Data
of INMET-Brazil

	A compilation of functions to download and processing AWS data of INMET-Brazil, with the purpose of reference evapotranspiration (ETo) estimation. The package aims to make meteorological and agricultural data analysis more parsimonious.
	"""
	
	cran = "BrazilMet" 

	version("0.2.0", md5="62519dcbc6a90f8e25e661a58ab29ec0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-dplyr@0.3.0.1:", type=("build", "run"))
