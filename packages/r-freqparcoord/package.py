# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFreqparcoord(RPackage):
	"""Novel Methods for Parallel Coordinates

	New approaches to parallel coordinates plots for
   multivariate data visualization, including applications to clustering,
   outlier hunting and regression diagnostics.  Includes general functions
   for multivariate nonparametric density and regression estimation, 
   using parallel computation.  
	"""
	
	cran = "freqparcoord" 

	version("1.0.1", md5="d87acfd8668af2bedb3d6ffbd69ec41a")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
