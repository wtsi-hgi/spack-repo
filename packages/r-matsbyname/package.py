# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMatsbyname(RPackage):
	"""An Implementation of Matrix Mathematics that Respects Row and
Column Names

	An implementation of matrix mathematics wherein operations are performed "by name."
	"""
	
	homepage = "https://github.com/MatthewHeun/matsbyname"
	cran = "matsbyname" 

	version("0.6.10", md5="fc86c90ef244e62f036d70b4dc67b809")

	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rclabels", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
