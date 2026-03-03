# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKraljicmatrix(RPackage):
	"""A Quantified Implementation of the Kraljic Matrix

	Implements a quantified approach to the Kraljic Matrix (Kraljic, 1983, <https://hbr.org/1983/09/purchasing-must-become-supply-management>)
    for strategically analyzing a firm’s purchasing portfolio. It combines multi-objective decision analysis to measure purchasing characteristics and
    uses this information to place products and services within the Kraljic Matrix.
	"""
	
	homepage = "https://github.com/koalaverse/KraljicMatrix"
	cran = "KraljicMatrix" 

	version("0.2.1", md5="284f5014d62411a04abe076c331be403")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
