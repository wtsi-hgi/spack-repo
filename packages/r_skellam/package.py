# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSkellam(RPackage):
	"""Densities and Sampling for the Skellam Distribution

	Functions for the Skellam distribution, including: density
    (pmf), cdf, quantiles and regression.
	"""
	
	homepage = "https//r-forge.r-project.org/projects/healthqueues/"
	cran = "skellam" 

	version("0.2.3", md5="325675bc249419f55e119f4b431b49b7")
	version("0.2.0", md5="e345942d5ccbfb718f08a4affe78d93a")

