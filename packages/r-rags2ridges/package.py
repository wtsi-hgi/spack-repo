# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRags2ridges(RPackage):
	"""Ridge Estimation of Precision Matrices from High-Dimensional
Data

	Proper L2-penalized maximum likelihood estimators for precision 
  matrices and supporting functions to employ these estimators in a graphical 
  modeling setting. For details, see Peeters, Bilgrau, & van Wieringen (2022) 
  <doi:10.18637/jss.v102.i04> and associated publications.
	"""
	
	homepage = "https://cfwp.github.io/rags2ridges/"
	cran = "rags2ridges" 

	version("2.2.7", md5="dbce30fb0683e62b76021b6141b4314e")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-grbase", type=("build", "run"))
	depends_on("r-rbgl", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
