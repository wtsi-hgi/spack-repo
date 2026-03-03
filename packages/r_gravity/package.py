# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGravity(RPackage):
	"""Estimation Methods for Gravity Models

	A wrapper of different standard estimation methods for gravity models. 
  This package provides estimation methods for log-log models and multiplicative models.
	"""
	
	homepage = "https://pacha.dev/gravity/"
	cran = "gravity" 

	version("1.1", md5="8ff8a773910ad8723a804efd111809ab")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-glm2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-censreg", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-multiwayvcov", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
