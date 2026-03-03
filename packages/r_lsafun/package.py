# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsafun(RPackage):
	"""Applied Latent Semantic Analysis (LSA) Functions

	Provides functions that allow for convenient working with vector space models of semantics/distributional semantic models/word embeddings. 
	Originally built for LSA models (hence the name), but can be used for all such vector-based models. 
	For actually building a vector semantic space, use the package 'lsa' or other specialized software. 
	Downloadable semantic spaces can be found at <https://sites.google.com/site/fritzgntr/software-resources>.
	"""
	
	cran = "LSAfun" 

	version("0.7.1", md5="0c0c62fd50d8bfa7b502149ce44ab2a3")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lsa", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
