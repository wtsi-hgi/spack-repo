# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlhd(RPackage):
	"""Maximin-Distance (Sliced) Latin Hypercube Designs

	Generate the optimal Latin Hypercube Designs (LHDs) for computer experiments with quantitative factors and the optimal Sliced Latin Hypercube Designs (SLHDs) for computer experiments with both quantitative and qualitative factors. Details of the algorithm can be found in Ba, S., Brenneman, W. A. and Myers, W. R. (2015), "Optimal Sliced Latin Hypercube Designs," Technometrics. Important function in this package is "maximinSLHD". 
	"""
	
	cran = "SLHD" 

	version("2.1-1", md5="439b94c763161c56302c730a32cd39af")

