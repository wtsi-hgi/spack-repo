# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCacc(RPackage):
	"""Conjunctive Analysis of Case Configurations

	A set of functions to conduct Conjunctive Analysis of Case Configurations (CACC) as described in Miethe, Hart, and Regoeczi (2008) <doi:10.1007/s10940-008-9044-8>, and identify and quantify situational clustering in dominant case configurations as described in Hart (2019) <doi:10.1177/0011128719866123>. Initially conceived as an exploratory technique for multivariate analysis of categorical data, CACC has developed to include formal statistical tests that can be applied in a wide variety of contexts. This technique allows examining composite profiles of different units of analysis in an alternative way to variable-oriented methods.
	"""
	
	homepage = "https://github.com/amoneva/cacc"
	cran = "cacc" 

	version("0.1.0", md5="786ba9167d33c54c5e31dce88ee29deb")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
