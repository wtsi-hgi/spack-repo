# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLingmatch(RPackage):
	"""Linguistic Matching and Accommodation

	Measure similarity between texts. Offers a variety of processing
  tools and similarity metrics to facilitate flexible representation of texts and matching.
  Implements forms of Language Style Matching (Ireland & Pennebaker, 2010) <doi:10.1037/a0020386>
  and Latent Semantic Analysis (Landauer & Dumais, 1997) <doi:10.1037/0033-295X.104.2.211>.
	"""
	
	homepage = "https://github.com/miserman/lingmatch"
	cran = "lingmatch" 

	version("1.0.6", md5="b0377d1397a3c5adebb48b5869796066")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
