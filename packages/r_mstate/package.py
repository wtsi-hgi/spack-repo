# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMstate(RPackage):
	"""Data Preparation, Estimation and Prediction in Multi-State
Models

	Contains functions for data preparation, descriptives, hazard estimation and prediction with Aalen-Johansen or simulation in competing risks and multi-state models, see Putter, Fiocco, Geskus (2007) <doi:10.1002/sim.2712>.
	"""
	
	homepage = "https://www.lumc.nl/org/bds/research/medische-statistiek/survival-analysis/"
	cran = "mstate" 

	version("0.3.2", md5="14aab86d42cc542dd73c96e279119ca9")

	depends_on("r-survival@3.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
