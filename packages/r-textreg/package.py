# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextreg(RPackage):
	"""n-Gram Text Regression, aka Concise Comparative Summarization

	Function for sparse regression on raw text, regressing a labeling
    vector onto a feature space consisting of all possible phrases.
	"""
	
	cran = "textreg" 

	version("0.1.5", md5="af0f1d584969a63705cb3dedf278149f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-tm@0.7:", type=("build", "run"))
	depends_on("r-nlp@0.1.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
