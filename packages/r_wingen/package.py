# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWingen(RPackage):
	"""Continuous Mapping of Genetic Diversity

	Generate continuous maps of genetic diversity using moving windows with options for rarefaction, interpolation, and masking as described in Bishop et al. (2023) <doi:10.1111/2041-210X.14090>.
	"""
	
	cran = "wingen" 

	version("2.1.1", md5="04e5c635c8d51bea0a40e61a20942caf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-automap", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
	depends_on("r-gdistance", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hierfstat", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pegas", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vcfr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
