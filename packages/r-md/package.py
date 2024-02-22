# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMd(RPackage):
	"""Selecting Bandwidth for Kernel Density Estimator with Minimum
Distance Method

	Selects bandwidth for the kernel density estimator with minimum distance method as proposed by Devroye and Lugosi (1996). The minimum distance method directly selects the optimal kernel density estimator from countably infinite kernel density estimators and indirectly selects the optimal bandwidth. This package selects the optimal bandwidth from finite kernel density estimators.
	"""
	
	cran = "md" 

	version("1.0.4", md5="51d3358a3de7712d4ee33aeea824f381")

