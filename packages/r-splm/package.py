# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplm(RPackage):
	"""Econometric Models for Spatial Panel Data

	ML and GM estimation and diagnostic testing of econometric models for spatial panel data.
	"""
	
	cran = "splm" 

	version("1.6-5", md5="004c91ac91bf5017ea1f529fc8ad5e70")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-plm", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-bdsmatrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-spatialreg@1.2.1:", type=("build", "run"))
	depends_on("r-spdep@1.2.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
