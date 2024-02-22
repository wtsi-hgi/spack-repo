# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPivmet(RPackage):
	"""Pivotal Methods for Bayesian Relabelling and k-Means Clustering

	Collection of pivotal algorithms 
             for: relabelling the MCMC chains in order to undo the label 
             switching problem in Bayesian mixture models;
             fitting sparse finite mixtures;
             initializing the centers of the classical k-means algorithm 
             in order to obtain a better clustering solution. 
             For further details see
             Egidi, Pappadà, Pauli and Torelli (2018b)<ISBN:9788891910233>.
	"""
	
	homepage = "https://github.com/leoegidi/pivmet"
	cran = "pivmet" 

	version("0.5.0", md5="233979a322d35a967a81499087025735")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-runjags", type=("build", "run"))
	depends_on("r-rstan", type=("build", "run"))
	depends_on("r-bayesmix", type=("build", "run"))
	depends_on("r-rjags", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-bayesplot", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
