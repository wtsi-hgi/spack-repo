# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCombinationpvalues(RPackage):
	"""Combination of Independent P-Values

	Provides access to six fundamental statistics that can be used for the purpose of combination p-values. All methods used can referenced here: Heard & Rubin-Delanchy (2017) <arXiv:1707.06897>.
	"""
	
	homepage = "https://github.com/StatsGirl/Master2021/tree/main/R"
	cran = "combinationpvalues" 

	version("0.1.4", md5="25fd6ffc94b4866152a7e286099dcda3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-chi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-spatstat-utils", type=("build", "run"))
