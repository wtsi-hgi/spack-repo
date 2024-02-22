# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantedaTextstats(RPackage):
	"""Textual Statistics for the Quantitative Analysis of Textual Data

	Textual statistics functions formerly in the 'quanteda' package.
    Textual statistics for characterizing and comparing textual data. Includes 
    functions for measuring term and document frequency, the co-occurrence of 
    words, similarity and distance between features and documents, feature entropy, 
    keyword occurrence, readability, and lexical diversity.  These functions 
    extend the 'quanteda' package and are specially designed for sparse textual data.
	"""
	
	homepage = "https://quanteda.io"
	cran = "quanteda.textstats" 

	version("0.96.4", md5="2650f2e3e6e0bf6fdb22f88ac813478c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quanteda", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
	depends_on("r-nsyllable", type=("build", "run"))
	depends_on("r-proxyc@0.1.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.600.1:", type=("build", "run"))
