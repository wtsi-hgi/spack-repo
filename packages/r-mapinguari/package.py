# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapinguari(RPackage):
	"""Process-Based Biogeographical Analysis

	Facilitates the incorporation of biological processes in biogeographical analyses. It offers conveniences in fitting, comparing and extrapolating models of biological processes such as physiology and phenology. These spatial extrapolations can be informative by themselves, but also complement traditional correlative species distribution models, by mixing environmental and process-based predictors. Caetano et al (2020) <doi:10.1111/oik.07123>.
	"""
	
	homepage = "https://github.com/gabrielhoc/Mapinguari"
	cran = "Mapinguari" 

	version("2.0.1", md5="ddbbf1c01daa115fbe7cd987a285359d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
