# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCondir(RPackage):
	"""Computation of P Values and Bayes Factors for Conditioning Data

	Set of functions for the easy analyses of conditioning data.
	"""
	
	homepage = "https://github.com/AngelosPsy/condir"
	cran = "condir" 

	version("0.1.4", md5="95eda1e2f078fac0bda24928074da67d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-bayesfactor@0.9.12:", type=("build", "run"))
	depends_on("r-knitr@1.28:", type=("build", "run"))
	depends_on("r-xtable@1.8.2:", type=("build", "run"))
	depends_on("r-psych@1.9.12:", type=("build", "run"))
	depends_on("r-effsize@0.7.8:", type=("build", "run"))
	depends_on("r-shiny@1.7:", type=("build", "run"))
