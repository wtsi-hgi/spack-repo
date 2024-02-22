# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuanteda(RPackage):
	"""Quantitative Analysis of Textual Data

	A fast, flexible, and comprehensive framework for 
    quantitative text analysis in R.  Provides functionality for corpus management,
    creating and manipulating tokens and n-grams, exploring keywords in context, 
    forming and manipulating sparse matrices
    of documents by features and feature co-occurrences, analyzing keywords, computing feature similarities and
    distances, applying content dictionaries, applying supervised and unsupervised machine learning, 
    visually representing text and text analyses, and more. 
	"""
	
	homepage = "https://quanteda.io"
	cran = "quanteda" 

	version("3.3.1", md5="b34e0169f0ac07848ecf17dc32585cd9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-stopwords", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.600.1:", type=("build", "run"))
