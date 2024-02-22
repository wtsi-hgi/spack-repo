# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrosamplingdesign(RPackage):
	"""Finding Optimal Microsampling Designs for Non-Compartmental
Pharmacokinetic Analysis

	
  Find optimal microsampling designs for non-compartmental pharacokinetic analysis using a  general simulation methodology:
  Algorithm III of Barnett, Helen, Helena Geys, Tom Jacobs, and Thomas Jaki. (2017) "Optimal Designs for Non-Compartmental
  Analysis of Pharmacokinetic Studies. (currently unpublished)"
  This methodology consist of (1) specifying a pharmacokinetic model
  including variability among animals; (2) generating possible sampling times; (3)
  evaluating performance of each time point choice on simulated data; (4)
  generating possible schemes given a time point choice and additional constraints
  and finally (5) evaluating scheme performance on simulated data. The default
  settings differ from the article of Barnett and others, in the default pharmacokinetic model used and
  the parameterization of variability among animals. Details can be found in the package vignette. A 'shiny'
  web application is included, which guides users from model parametrization to
  optimal microsampling scheme.   
	"""
	
	homepage = "https://www.openanalytics.eu/"
	cran = "microsamplingDesign" 

	version("1.0.8", md5="6b6eccd701b3b62adf5dc6e4195e55f2")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
