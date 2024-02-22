# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScoring(RPackage):
	"""Proper Scoring Rules

	Evaluating probabilistic forecasts via proper scoring rules.  scoring implements the beta, power, and pseudospherical families of proper scoring rules, along with ordered versions of the latter two families.  Included among these families are popular rules like the Brier (quadratic) score, logarithmic score, and spherical score.  For two-alternative forecasts, also includes functionality for plotting scores that one would obtain under specific scoring rules.
	"""
	
	cran = "scoring" 

	version("0.6", md5="0ed511b57eed5a1848cd389cdd9357ca")

