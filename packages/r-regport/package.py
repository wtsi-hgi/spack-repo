# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRegport(RPackage):
	"""Regression Model Processing Port

	Provides R6 classes, methods and utilities to construct,
    analyze, summarize, and visualize regression models.
	"""
	
	homepage = "https://github.com/ShixiangWang/regport"
	cran = "regport" 

	version("0.3.0", md5="2f269e9265dd2013f4beef9c2a84c3d0")

	depends_on("r-broom-helpers", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forestploter", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-parameters", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
