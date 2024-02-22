# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlintyr(RPackage):
	"""Simple and Flexible Tests of Sample Exchangeability

	Given a multivariate dataset and some knowledge about the dependencies 
              between its features, it is customary to fit a statistical model to the features 
              to infer parameters of interest. Such a procedure implicitly assumes that the 
              sample is exchangeable. This package provides a flexible non-parametric test 
              of this exchangeability assumption, allowing the user to specify the feature 
              dependencies by hand as long as features can be grouped into disjoint independent sets. 
              This package also allows users to test a dual hypothesis, which is, given that the 
              sample is exchangeable, does a proposed grouping of the features into disjoint sets
              also produce statistically independent sets of features? See Aw, Spence and Song (2023) 
              for the accompanying paper.
	"""
	
	homepage = "https://alanaw1.github.io/flintyR/"
	cran = "flintyR" 

	version("0.1.0", md5="3bfb8459c991a545aa2000c3eb5ecb93")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
