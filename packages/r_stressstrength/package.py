# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStressstrength(RPackage):
	"""Computation and Estimation of Reliability of Stress-Strength
Models

	Reliability of (normal) stress-strength models and for building two-sided or one-sided confidence intervals according to different approximate procedures.
	"""
	
	cran = "StressStrength" 

	version("1.0.2", md5="f2661703bbe8d868a64331b2bed15e99")

