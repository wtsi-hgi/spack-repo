# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimilar(RPackage):
	"""R Source Code Similarity Evaluation

	An implementation of a novel method to quantify the similarity
    of the code-base of R functions by means of program dependence graphs.
    Possible use cases include detection of code clones for improving
    software quality and of plagiarism amongst students' assignments.
	"""
	
	homepage = "https://github.com/bartoszukm/SimilaR"
	cran = "SimilaR" 

	version("1.0.8", md5="886770038999417eaeaaa72e0eb1f9a0")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp@0.12:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
