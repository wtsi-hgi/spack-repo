# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTexttinyr(RPackage):
	"""Text Processing for Small or Big Data Files

	It offers functions for splitting, parsing, tokenizing and creating a vocabulary for big text data files. Moreover, it includes functions for building a document-term matrix and extracting information from those (term-associations, most frequent terms). It also embodies functions for calculating token statistics (collocations, look-up tables, string dissimilarities) and functions to work with sparse matrices. Lastly, it includes functions for Word Vector Representations (i.e. 'GloVe', 'fasttext') and incorporates functions for the calculation of (pairwise) text document dissimilarities. The source code is based on 'C++11' and exported in R through the 'Rcpp', 'RcppArmadillo' and 'BH' packages.
	"""
	
	homepage = "https://github.com/mlampros/textTinyR"
	cran = "textTinyR" 

	version("1.1.8", md5="5eefadbbcdc58dc88d9c3b5eb87c5580")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.8:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("armadillo", type=("build", "link", "run"))
