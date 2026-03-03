# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcmabc(RPackage):
	"""Approximate Bayesian Computations for Phylogenetic Comparative
Methods

	Fits by ABC, the parameters of a stochastic process modelling the phylogeny and evolution of a suite of traits following the tree. The user may define an arbitrary Markov process for the trait and phylogeny. Importantly, trait-dependent speciation models are handled and fitted to data. See K. Bartoszek, P. Lio' (2019) <doi:10.5506/APhysPolBSupp.12.25>. The suggested geiger package can be obtained from CRAN's archive <https://cran.r-project.org/src/contrib/Archive/geiger/>, suggested to take latest version. Otherwise its required code is present in the pcmabc package. The suggested distory package can be obtained from CRAN's archive <https://cran.r-project.org/src/contrib/Archive/distory/>, suggested to take latest version. 
	"""
	
	cran = "pcmabc" 

	version("1.1.3", md5="fe7421c77851ecf7a6bca64311c37262")

	depends_on("r@2.9.1:", type=("build", "run"))
	depends_on("r-ape@3.0.6:", type=("build", "run"))
	depends_on("r-mvslouch", type=("build", "run"))
	depends_on("r-phangorn", type=("build", "run"))
	depends_on("r-yuima", type=("build", "run"))
