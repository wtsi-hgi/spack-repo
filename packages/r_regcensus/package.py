# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegcensus(RPackage):
	"""Accessing Data from the 'RegCensusAPI'

	Allowing users to access data from the 'RegCensusAPI'. The 'RegCensusAPI' is an API client that connects to the 'RegData' regulatory restrictions data by the 'Mercatus Center' at 'George Mason University'. 'RegData' uses machine learning algorithms to quantify the number of regulatory restrictions in a jurisdiction. You can find out more about 'RegData' from 'QuantGov website' <https://www.quantgov.org>.
	"""
	
	homepage = "https://github.com/QuantGov/regcensus-api-R"
	cran = "regcensus" 

	version("1.0.1", md5="1da7f4d263e2decb0153892ee7011df2")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
