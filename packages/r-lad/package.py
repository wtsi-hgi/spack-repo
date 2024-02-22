# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLad(RPackage):
	"""Derive Leaf Angle Distribution (LAD) from Measured Leaf
Inclination Angles

	Calculate mean statistics and leaf angle distribution type from measured leaf inclination angles. LAD distribution is fitted using a two-parameters (mu, nu) Beta distribution and compared with six theoretical LAD distributions. Additional information is provided in Chianucci and Cesaretti (2022) <doi:10.1101/2022.10.28.513998>.
	"""
	
	cran = "LAD" 

	version("0.1.0", md5="f6f24982208ee4a1d72d0462896e0c03")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
