# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBdgraph(RPackage):
	"""Bayesian Structure Learning in Graphical Models using
Birth-Death MCMC

	Statistical tools for Bayesian structure learning in undirected graphical models for continuous, ordinal/discrete/count, and mixed data. The package is implemented the recent improvements in the Bayesian graphical models' literature, including Mohammadi and Wit (2015) <doi:10.1214/14-BA889>, Mohammadi et al. (2021) <doi:10.1080/01621459.2021.1996377>, and Dobra and Mohammadi (2018) <doi:10.1214/18-AOAS1164>. 
	"""
	
	homepage = "https://www.uva.nl/profile/a.mohammadi"
	cran = "BDgraph" 

	version("2.72", md5="bdb416a2bb41111c491864e56352e55b")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
