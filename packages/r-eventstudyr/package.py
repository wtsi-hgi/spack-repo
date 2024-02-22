# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REventstudyr(RPackage):
	"""Estimation and Visualization of Linear Panel Event Studies

	Estimates linear panel event study models. Plots coefficients following the recommendations in Freyaldenhoven et al. (2021) <doi:10.3386/w29170>. Includes sup-t bands, testing for key hypotheses, least wiggly path through the Wald region. Allows instrumental variables estimation following Freyaldenhoven et al. (2019) <doi:10.1257/aer.20180609>.
	"""
	
	homepage = "https://github.com/JMSLab/eventstudyr"
	cran = "eventstudyr" 

	version("1.1.2", md5="5f8ea32c66e3d29f602de2f35710af6a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-estimatr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
