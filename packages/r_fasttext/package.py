# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFasttext(RPackage):
	"""Efficient Learning of Word Representations and Sentence
Classification

	An interface to the 'fastText' <https://github.com/facebookresearch/fastText> library for efficient learning of word representations and sentence classification. The 'fastText' algorithm is explained in detail in (i) "Enriching Word Vectors with subword Information", Piotr Bojanowski, Edouard Grave, Armand Joulin, Tomas Mikolov, 2017, <doi:10.1162/tacl_a_00051>; (ii) "Bag of Tricks for Efficient Text Classification", Armand Joulin, Edouard Grave, Piotr Bojanowski, Tomas Mikolov, 2017, <doi:10.18653/v1/e17-2068>; (iii) "FastText.zip: Compressing text classification models", Armand Joulin, Edouard Grave, Piotr Bojanowski, Matthijs Douze, Herve Jegou, Tomas Mikolov, 2016, <arXiv:1612.03651>.
	"""
	
	homepage = "https://github.com/mlampros/fastText"
	cran = "fastText" 

	version("1.0.4", md5="9f2305578b20c73a1b5d10ef639141b0")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
