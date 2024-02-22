# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMazamarollutils(RPackage):
	"""Efficient Rolling Functions

	A suite of compiled functions calculating rolling mins, means, 
    maxes and other statistics. This package is designed to meet the needs of
    data processing systems for environmental time series.
	"""
	
	homepage = "https://github.com/MazamaScience/MazamaRollUtils"
	cran = "MazamaRollUtils" 

	version("0.1.3", md5="c0f5b4200e903112666f0b216e8ccb8d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
