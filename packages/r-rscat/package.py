# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRscat(RPackage):
	"""Shadow-Test Approach to Computerized Adaptive Testing

	As an advanced approach to computerized adaptive testing (CAT), 
  shadow testing (van der Linden(2005) <doi:10.1007/0-387-29054-0>) dynamically 
  assembles entire shadow tests as a part of 
  selecting items throughout the testing process.
  Selecting items from shadow tests guarantees the compliance of all content 
  constraints defined by the blueprint. 'RSCAT' is an R package for the 
  shadow-test approach to CAT. The objective of 
  'RSCAT' is twofold: 1) Enhancing the effectiveness of shadow-test CAT simulation;
  2) Contributing to the academic and scientific community for CAT research.
  RSCAT is currently designed for dichotomous items based on the three-parameter logistic (3PL) model.
	"""
	
	cran = "RSCAT" 

	version("1.1.3", md5="b40bacd1216af0868e40be3714ddf8e7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
