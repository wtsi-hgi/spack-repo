# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextminer(RPackage):
	"""Functions for Text Mining and Topic Modeling

	An aid for text mining in R, with a syntax that
    should be familiar to experienced R users. Provides a wrapper for several 
    topic models that take similarly-formatted input and give similarly-formatted
    output. Has additional functionality for analyzing and diagnostics for
    topic models.
	"""
	
	homepage = "https://www.rtextminer.com/"
	cran = "textmineR" 

	version("3.0.5", md5="953e04ea51b2846a5d0082884591b25b")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-text2vec@0.5:", type=("build", "run"))
	depends_on("r-stopwords", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
