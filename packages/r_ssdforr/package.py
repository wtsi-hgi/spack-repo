# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsdforr(RPackage):
	"""Functions to Analyze Single System Data

	Functions to visually and statistically analyze single system data.
	"""
	
	cran = "SSDforR" 

	version("1.5.34", md5="308951e1be311d00a2c1a22c9a2290e2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-ttr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mad", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
	depends_on("r-singlecasees", type=("build", "run"))
	depends_on("r-kendall", type=("build", "run"))
	depends_on("r-modifiedmk", type=("build", "run"))
