# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArpsdca(RPackage):
	"""Arps Decline Curve Analysis in R

	Functions for Arps decline-curve analysis on oil and gas data. Includes exponential, hyperbolic, harmonic, and hyperbolic-to-exponential models as well as the preceding with initial curtailment or a period of linear rate buildup. Functions included for computing rate, cumulative production, instantaneous decline, EUR, time to economic limit, and performing least-squares best fits.
	"""
	
	homepage = "https://github.com/derrickturk/aRpsDCA"
	cran = "aRpsDCA" 

	version("1.1.1", md5="5ea4c018692921c9bad08e4d72f8a1df")

