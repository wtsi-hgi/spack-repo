# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCabootcrs(RPackage):
	"""Bootstrap Confidence Regions for Simple and Multiple
Correspondence Analysis

	Performs simple correspondence analysis on a two-way contingency table, 
    or multiple correspondence analysis (homogeneity analysis) 
    on data with p categorical variables,
    and produces bootstrap-based elliptical confidence regions around the 
    projected coordinates for the category points. 
    Includes routines to plot the results in a variety of styles. 
    Also reports the standard numerical output for correspondence analysis.
	"""
	
	cran = "cabootcrs" 

	version("2.1.0", md5="3d1c2dbec2d6279332e286cae883b1a2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
