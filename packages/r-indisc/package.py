# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndisc(RPackage):
	"""Obtaining and Estimating Unidimensional and Multidimensional IRT
Dual Models

	Performs a unified approach for obtaining and estimating
    unidimensional  and multidimensional Item Response Theory (IRT) 
    Dual Models (DMs), proposed by Ferrando (2019 <doi:10.1177/0146621618817779>).
	"""
	
	cran = "InDisc" 

	version("1.1.0", md5="0dc6773698f165f6d5d0ef70cf8d588f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
