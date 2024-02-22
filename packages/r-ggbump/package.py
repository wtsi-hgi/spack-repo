# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgbump(RPackage):
	"""Bump Chart and Sigmoid Curves

	A geom for ggplot to create bump plots. Can be good to use for showing rank over time.
	"""
	
	cran = "ggbump" 

	version("0.1.0", md5="1ec6860e19e80a6b489d12fcdb1b55c1")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
