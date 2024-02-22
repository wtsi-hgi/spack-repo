# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REzmmek(RPackage):
	"""Easy Michaelis-Menten Enzyme Kinetics

	Serves as a platform for published fluorometric enzyme assay
 protocols. 'ezmmek' calibrates, calculates, and plots enzyme activities as they
 relate to the transformation of synthetic substrates. At present, 'ezmmek'
 implements two common protocols found in the literature, and is modular to accommodate
 additional protocols. Here, these protocols are referred to as the In-Sample
 Calibration (Hoppe, 1983; <doi:10.3354/meps011299>) and In-Buffer Calibration (German et al., 2011; <doi:10.1016/j.soilbio.2011.03.017>).
 protocols. By containing multiple protocols, 'ezmmek' aims to stimulate
 discussion about how to best optimize fluorometric enzyme assays. A standardized
 approach would make studies more comparable and reproducible. 
	"""
	
	cran = "ezmmek" 

	version("0.2.4", md5="8a5fa371507999b4285b28ba8db39def")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-assertable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-nls2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
