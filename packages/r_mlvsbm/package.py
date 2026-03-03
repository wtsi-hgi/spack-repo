# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlvsbm(RPackage):
	"""A Stochastic Block Model for Multilevel Networks

	Simulation, inference and clustering of multilevel networks using a
    Stochastic Block Model framework as described in Chabert-Liddell, Barbillon,
    Donnet and Lazega (2021) <doi:10.1016/j.csda.2021.107179>. 
    A multilevel network is defined as the junction of two interaction networks, 
    the upper level or inter-organizational level and the lower level or 
    inter-individual level. The inter-level represents an affiliation 
    relationship.
	"""
	
	homepage = "https://github.com/Chabert-Liddell/MLVSBM"
	cran = "MLVSBM" 

	version("0.2.4", md5="03e9c7aa17d569a468ce62725b1ffd16")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-blockmodels", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
