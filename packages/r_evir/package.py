# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvir(RPackage):
	"""Extreme Values in R

	Functions for extreme value theory, which may be 
  divided into the following groups; exploratory data analysis, 
  block maxima, peaks over thresholds (univariate and bivariate), 
  point processes, gev/gpd distributions.
	"""
	
	cran = "evir" 

	version("1.7-4", md5="7168004b08cbea36e74cde9ee9821bff")

