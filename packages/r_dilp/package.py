# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDilp(RPackage):
	"""Reconstruct Paleoclimate and Paleoecology with Leaf Physiognomy

	Use leaf physiognomic methods to reconstruct mean annual
    temperature (MAT), mean annual precipitation (MAP), and leaf dry mass
    per area (Ma), along with other useful quantitative leaf traits. Methods
    in this package described in Lowe et al. (in review).
	"""
	
	homepage = "https://github.com/mjbutrim/dilp"
	cran = "dilp" 

	version("1.0.0", md5="1f276d3e9caeb9f325cf0283ccc60b64")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
