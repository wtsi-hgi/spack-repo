# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustorus(RPackage):
	"""Prediction and Clustering on the Torus by Conformal Prediction

	Provides various tools of for clustering multivariate angular 
  data on the torus. The package provides angular 
  adaptations of usual clustering methods such as the k-means 
  clustering, pairwise angular distances, which can be used as an 
  input for distance-based clustering algorithms, and implements
  clustering based on the conformal prediction framework. Options 
  for the conformal scores include scores based on a kernel density 
  estimate, multivariate von Mises mixtures, and naive k-means clusters. 
  Moreover, the package provides some basic data handling tools for 
  angular data.
	"""
	
	homepage = "https://github.com/sungkyujung/ClusTorus"
	cran = "ClusTorus" 

	version("0.2.2", md5="92965256ac517f0be15370e3bc199319")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bambi", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
