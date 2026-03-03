# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScplot(RPackage):
	"""Plot Function for Single-Case Data Frames

	Add-on for the 'scan' package that creates plots 
  from single-case data frames ('scdf'). It includes functions for styling 
  single-case plots, adding phase-based lines to indicate various statistical 
  parameters, and predefined themes for presentations and publications. More 
  information and in depth examples can be found in the online book 
  "Analyzing Single-Case Data with R and 'scan" 
  Jürgen Wilbert (2023) <https://jazznbass.github.io/scan-Book/>.
	"""
	
	cran = "scplot" 

	version("0.3.3", md5="0eaa1e22c8dd8827315232c377e74556")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scan@0.57:", type=("build", "run"))
	depends_on("r-mblm", type=("build", "run"))
