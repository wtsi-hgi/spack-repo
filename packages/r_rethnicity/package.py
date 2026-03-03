# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRethnicity(RPackage):
	"""Predicting Ethnic Group from Names

	Implementation of the race/ethnicity prediction method, described 
    in "rethnicity: An R package for predicting ethnicity from names" 
    by Fangzhou Xie (2022) <doi:10.1016/j.softx.2021.100965> and 
    "Rethnicity: Predicting Ethnicity from Names" by Fangzhou Xie (2021) <arXiv:2109.09228>.
	"""
	
	homepage = "https://github.com/fangzhou-xie/rethnicity"
	cran = "rethnicity" 

	version("0.2.4", md5="c74d3f6e5f49e2faeb5978301dd0f7e0")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppthread@2.1.3:", type=("build", "run"))
