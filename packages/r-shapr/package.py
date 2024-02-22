# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShapr(RPackage):
	"""Prediction Explanation with Dependence-Aware Shapley Values

	Complex machine learning models are often hard to interpret. However, in 
  many situations it is crucial to understand and explain why a model made a specific 
  prediction. Shapley values is the only method for such prediction explanation framework 
  with a solid theoretical foundation. Previously known methods for estimating the Shapley 
  values do, however, assume feature independence. This package implements the method 
  described in Aas, Jullum and Løland (2019) <arXiv:1903.10464>, which accounts for any feature 
  dependence, and thereby produces more accurate estimates of the true Shapley values.
	"""
	
	homepage = "https://norskregnesentral.github.io/shapr/"
	cran = "shapr" 

	version("0.2.2", md5="d13fbd983cb829b2b75eec11f124fbf4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-condmvnorm", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
