# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REga(RPackage):
	"""Error Grid Analysis

	Functions for assigning Clarke or Parkes (Consensus) error grid
    zones to blood glucose values, and for plotting both types of error grids
    in both mg/mL and mmol/L units.
	"""
	
	cran = "ega" 

	version("2.0.0", md5="9fa4c44ff78c4c86cb145e40e946e41f")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
