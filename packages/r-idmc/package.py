# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdmc(RPackage):
	"""Load and Wrangle IDMC Displacement Data

	Utilities to work with data from the Internal Displacement
    Monitoring Centre (IDMC), with convenient functions for loading events
    data from the IDMC API and transforming events data to daily
    displacement estimates.
	"""
	
	homepage = "https://github.com/ocha-dap/idmc"
	cran = "idmc" 

	version("0.3.0", md5="544958c8e0a8868a01651317254950d3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
