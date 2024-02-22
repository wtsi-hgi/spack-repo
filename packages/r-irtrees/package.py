# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrtrees(RPackage):
	"""Estimation of Tree-Based Item Response Models

	Helper functions and example data sets to facilitate the estimation of IRTree models from data with different shape and using different software.
	"""
	
	cran = "irtrees" 

	version("1.0.0", md5="9110fd81d12c0288cb448898243557ce")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
