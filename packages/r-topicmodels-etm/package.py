# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTopicmodelsEtm(RPackage):
	"""Topic Modelling in Embedding Spaces

	Find topics in texts which are semantically embedded using techniques like word2vec or Glove. 
    This topic modelling technique models each word with a categorical distribution whose natural parameter is the inner product between a word embedding and an embedding of its assigned topic.
    The techniques are explained in detail in the paper 'Topic Modeling in Embedding Spaces' by Adji B. Dieng, Francisco J. R. Ruiz, David M. Blei (2019), available at <arXiv:1907.04907>.
	"""
	
	cran = "topicmodels.etm" 

	version("0.1.0", md5="558cb74547fbd84f3441e38da5699882")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-torch@0.5:", type=("build", "run"))
	depends_on("py-torch", type=("build", "link", "run"))
