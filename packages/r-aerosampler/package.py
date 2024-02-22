# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAerosampler(RPackage):
	"""Estimate Aerosol Particle Collection Through Sample Lines

	Estimate ideal efficiencies of aerosol sampling through sample
    lines. Functions were developed consistent with the approach described in 
    Hogue, Mark; Thompson, Martha; Farfan, Eduardo; Hadlock, Dennis, (2014), 
    "Hand Calculations for Transport of Radioactive Aerosols through Sampling 
    Systems" Health Phys 106, 5, S78-S87, <doi:10.1097/HP.0000000000000092>.
	"""
	
	cran = "AeroSampleR" 

	version("0.2.0", md5="52b5d1843af785abd0dc51da53f16507")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
