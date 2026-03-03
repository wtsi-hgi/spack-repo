# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTapnet(RPackage):
	"""Trait Matching and Abundance for Predicting Bipartite Networks

	Functions to produce, fit and predict from bipartite networks with abundance, trait and phylogenetic information. Its methods are described in detail in Benadi, G., Dormann, C.F., Fruend, J., Stephan, R. & Vazquez, D.P. (2021) Quantitative prediction of interactions in bipartite networks based on traits, abundances, and phylogeny. The American Naturalist, in press.
	"""
	
	homepage = "https://github.com/biometry/tapnet"
	cran = "tapnet" 

	version("0.3", md5="d74917c242046c7da3b70c46f7444fd5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-bipartite", type=("build", "run"))
	depends_on("r-mpsem", type=("build", "run"))
	depends_on("r-phytools", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
