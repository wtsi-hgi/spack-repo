# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdpuc(RPackage):
	"""Easily Convert GDP Data

	Convert GDP time series data from one unit to
    another. All common GDP units are included, i.e. current and constant
    local currency units, US$ via market exchange rates and international
    dollars via purchasing power parities. 
	"""
	
	homepage = "https://github.com/pik-piam/GDPuc"
	cran = "GDPuc" 

	version("0.11.1", md5="f90586881a20330a993f86a901d79254")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli@2.4:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
