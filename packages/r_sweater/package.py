# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSweater(RPackage):
	"""Speedy Word Embedding Association Test and Extras Using R

	Conduct various tests for evaluating implicit biases in word embeddings: Word Embedding Association Test (Caliskan et al., 2017), <doi:10.1126/science.aal4230>, Relative Norm Distance (Garg et al., 2018), <doi:10.1073/pnas.1720347115>, Mean Average Cosine Similarity (Mazini et al., 2019) <arXiv:1904.04047>, SemAxis (An et al., 2018) <arXiv:1806.05521>, Relative Negative Sentiment Bias (Sweeney & Najafian, 2019) <doi:10.18653/v1/P19-1162>, and Embedding Coherence Test (Dev & Phillips, 2019) <arXiv:1901.07656>.
	"""
	
	homepage = "https://github.com/gesistsa/sweater"
	cran = "sweater" 

	version("0.1.8", md5="167c0f78796974dfafc49d34cab8d6ae")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-liblinear", type=("build", "run"))
	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
