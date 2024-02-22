# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWord2vec(RPackage):
	"""Distributed Representations of Words

	Learn vector representations of words by continuous bag of words and skip-gram implementations of the 'word2vec' algorithm. 
    The techniques are detailed in the paper "Distributed Representations of Words and Phrases and their Compositionality" by Mikolov et al. (2013), available at <arXiv:1310.4546>.
	"""
	
	homepage = "https://github.com/bnosac/word2vec"
	cran = "word2vec" 

	version("0.4.0", md5="2fa2b87d0b3041086da4fd50135cbc4a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
