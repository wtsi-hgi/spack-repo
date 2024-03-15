# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdapplied(RPackage):
	"""Machine Learning and Inference for Topological Data Analysis

	Topological data analysis is a powerful tool for finding non-linear global structure
    in whole datasets. The main tool of topological data analysis is persistent homology, which computes
    a topological shape descriptor of a dataset called a persistence diagram. 'TDApplied' provides 
    useful and efficient methods for analyzing groups of persistence diagrams with machine learning and statistical inference,
    and these functions can also interface with other data science packages to form flexible and integrated
    topological data analysis pipelines.
	"""
	
	homepage = "https://github.com/shaelebrown/TDApplied"
	cran = "TDApplied" 

	version("3.0.3", md5="798076d6e5fbd5e795ecefeba1b08a1a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-rdist", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
