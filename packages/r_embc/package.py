# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmbc(RPackage):
	"""Expectation-Maximization Binary Clustering

	Unsupervised, multivariate, binary clustering for meaningful annotation of data, taking into account the uncertainty in the data. A specific constructor for trajectory analysis in movement ecology yields behavioural annotation of trajectories based on estimated local measures of velocity and turning angle, eventually with solar position covariate as a daytime indicator, ("Expectation-Maximization Binary Clustering for Behavioural Annotation").
	"""
	
	homepage = "<doi:10.1371/journal.pone.0151984>"
	cran = "EMbC" 

	version("2.0.4", md5="0229c2e1bc3aea63856e6d4386597b29")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-suntools", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
