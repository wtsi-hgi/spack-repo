# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REquate(RPackage):
	"""Observed-Score Linking and Equating

	Contains methods for observed-score linking
  and equating under the single-group, equivalent-groups,
  and nonequivalent-groups with anchor test(s) designs.
  Equating types include identity, mean, linear, general
  linear, equipercentile, circle-arc, and composites of
  these. Equating methods include synthetic, nominal
  weights, Tucker, Levine observed score, Levine true
  score, Braun/Holland, frequency estimation, and chained
  equating. Plotting and summary methods, and methods for
  multivariate presmoothing and bootstrap error estimation
  are also provided.
	"""
	
	homepage = "https://github.com/talbano/equate"
	cran = "equate" 

	version("2.0.8", md5="355cb1375d9bc632232ea4f536b66979")

	depends_on("r@4.1:", type=("build", "run"))
