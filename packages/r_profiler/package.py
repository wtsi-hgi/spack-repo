# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProfiler(RPackage):
	"""Profile Analysis of Multivariate Data in R

	A suite of multivariate methods and data visualization 
      tools to implement profile analysis and cross-validation techniques described in 
      Davison & Davenport (2002) <DOI: 10.1037/1082-989X.7.4.468>, Bulut (2013), and other published and unpublished resources.
      The package includes routines to perform criterion-related profile analysis, profile analysis 
      via multidimensional scaling, moderated profile analysis, profile analysis by group, and a 
      within-person factor model to derive score profiles.
	"""
	
	cran = "profileR" 

	version("0.3-5", md5="001e3e86920b06062af3c5e4dffdd0dd")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r@3:", type=("build", "run"))
