# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurveytable(RPackage):
	"""Formatted Survey Estimates

	Short and understandable commands that generate tabulated, 
    formatted, and rounded survey estimates. Mostly a wrapper for the 
    'survey' package (Lumley (2004) <doi:10.18637/jss.v009.i08> 
    <https://CRAN.R-project.org/package=survey>) that implements the National 
    Center for Health Statistics (NCHS) presentation standards 
    (Parker et al. (2017) <https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf>,
    Parker et al. (2023) <doi:10.15620/cdc:124368>).
	"""
	
	homepage = "https://cdcgov.github.io/surveytable/"
	cran = "surveytable" 

	version("0.9.2", md5="05a723535a842f73ea01bcbb2371d305")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-huxtable", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
