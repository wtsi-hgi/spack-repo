# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWineq(RPackage):
	"""Inequality Measures for Weighted Data

	Computes inequality measures of a given variable taking into account weights. Bootstrap method provides distribution of inequality measures and several additional statistics. 
	"""
	
	cran = "wINEQ" 

	version("1.2.0", md5="f4abc9bc05288714fcba79b85c972291")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
