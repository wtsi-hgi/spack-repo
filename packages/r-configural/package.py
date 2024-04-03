# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfigural(RPackage):
	"""Multivariate Profile Analysis

	R functions for criterion profile analysis, Davison and Davenport (2002) <doi:10.1037/1082-989X.7.4.468> and meta-analytic criterion profile analysis, Wiernik, Wilmot, Davison, and Ones (2020) <doi:10.1037/met0000305>. Sensitivity analyses to aid in interpreting criterion profile analysis results are also included.
	"""
	
	cran = "configural" 

	version("0.1.4", md5="5ed92d887c384e4712ede075dbdc6bdf")
	version("0.1.5", md5="f09157c9d7169d2fb06f21c267735d01")

	depends_on("r@3.4:", type=("build", "run"))
