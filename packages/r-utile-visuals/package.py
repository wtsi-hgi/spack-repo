# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUtileVisuals(RPackage):
	"""Create Visuals for Publication

	A set of functions to aid in the production of visuals in ggplot2.
	"""
	
	homepage = "https://efinite.github.io/utile.visuals/"
	cran = "utile.visuals" 

	version("0.3.3", md5="d12cfb34d6a94278e9bc1d22e863e170")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2@0.3.4:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
