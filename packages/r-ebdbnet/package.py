# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbdbnet(RPackage):
	"""Empirical Bayes Estimation of Dynamic Bayesian Networks

	Infer the adjacency matrix of a
	network from time course data using an empirical Bayes
	estimation procedure based on Dynamic Bayesian Networks.
	"""
	
	homepage = "https://github.com/andreamrau/ebdbNet"
	cran = "ebdbNet" 

	version("1.2.8", md5="c3080a14447083458dfe17e3efeaf707")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
