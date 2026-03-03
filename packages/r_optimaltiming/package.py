# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimaltiming(RPackage):
	"""Optimal Timing Identification

	Identify the optimal timing for new treatment initiation during multiple state disease transition, including  multistate model fitting, simulation of mean residual lifetime for a given transition state, and estimation of confidence interval. The method is referred to de Wreede, L., Fiocco, M., & Putter, H. (2011) <doi:10.18637/jss.v038.i07>.
	"""
	
	cran = "OptimalTiming" 

	version("0.1.0", md5="ff2937f987d52a0e7f8ab02cedd678f0")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mstate", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
