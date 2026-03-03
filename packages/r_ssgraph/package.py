# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsgraph(RPackage):
	"""Bayesian Graph Structure Learning using Spike-and-Slab Priors

	Bayesian estimation for undirected graphical models using spike-and-slab priors. The package handles continuous, discrete, and mixed data. 
	"""
	
	homepage = "https://www.uva.nl/profile/a.mohammadi"
	cran = "ssgraph" 

	version("1.15", md5="37bc9901a7d89f02d711989f9f8d2ebd")

	depends_on("r-bdgraph@2.58:", type=("build", "run"))
