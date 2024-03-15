# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuimtehol(RPackage):
	"""Learn Text 'Embeddings' with 'Starspace'

	Wraps the 'StarSpace' library <https://github.com/facebookresearch/StarSpace> 
    allowing users to calculate word, sentence, article, document, webpage, link and entity 'embeddings'. 
    By using the 'embeddings', you can perform text based multi-label classification, 
    find similarities between texts and categories, do collaborative-filtering based recommendation 
    as well as content-based recommendation, find out relations between entities, calculate 
    graph 'embeddings' as well as perform semi-supervised learning and multi-task learning on plain text. 
    The techniques are explained in detail in the paper: 'StarSpace: Embed All The Things!' by Wu et al. (2017), available at <arXiv:1709.03856>.
	"""
	
	homepage = "https://github.com/bnosac/ruimtehol"
	cran = "ruimtehol" 

	version("0.3.2", md5="251c35623367f1fd7ce8658fec18f272")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
