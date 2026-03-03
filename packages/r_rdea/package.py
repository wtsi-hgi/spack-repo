# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdea(RPackage):
	"""Robust Data Envelopment Analysis (DEA) for R

	Data Envelopment Analysis for R, estimating robust DEA scores without and with environmental variables and doing returns-to-scale tests.
	"""
	
	homepage = "https://github.com/jaak-s/rDEA"
	cran = "rDEA" 

	version("1.2-8", md5="d6c2c24dda2a54090f5417d5f816b398")

	depends_on("r-slam@0.1.9:", type=("build", "run"))
	depends_on("r-truncreg@0.2.1:", type=("build", "run"))
	depends_on("r-truncnorm@1.0.7:", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("glpk@4.52:", type=("build", "link", "run"))
