# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REstatapi(RPackage):
	"""R Interface to e-Stat API

	Provides an interface to e-Stat API, the one-stop service for official statistics of the Japanese government.
	"""
	
	homepage = "https://yutannihilation.github.io/estatapi/"
	cran = "estatapi" 

	version("0.4.0", md5="32a9dd6be9ffcbafc2595b2bf766b9c0")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-purrr@0.2:", type=("build", "run"))
	depends_on("r-readr@0.2:", type=("build", "run"))
	depends_on("r-dplyr@0.5:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
