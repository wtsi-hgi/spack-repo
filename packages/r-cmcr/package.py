# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCmcr(RPackage):
	"""An Implementation of the 'Congruent Matching Cells' Method

	An open-source implementation of the 'Congruent Matching Cells' 
    method for cartridge case identification as proposed by Song (2013) <https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=911193> as well 
    as an extension of the method proposed by Tong et al. (2015) <doi:10.6028/jres.120.008>.
    Provides a wide range of pre, inter, and post-processing options when
    working with cartridge case scan data and their associated comparisons. See
    the cmcR package website for more details and examples.
	"""
	
	cran = "cmcR" 

	version("0.1.11", md5="61b83e78838b8baee8f10c12023227ad")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-x3ptools", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@3.3.5:", type=("build", "run"))
	depends_on("r-imager", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-ggnewscale@0.4.6:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
